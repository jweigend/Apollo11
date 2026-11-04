"""Render the README teaser video: drive the project's 3D viewer page frame by frame in
headless Chromium, add captions, write PNG frames, then encode them with ffmpeg.

Needs Playwright (not a project dependency):

    python3 -m venv /tmp/teaser-venv && /tmp/teaser-venv/bin/pip install playwright
    /tmp/teaser-venv/bin/playwright install chromium
    /tmp/teaser-venv/bin/python tools/render_teaser.py . /tmp/teaser-frames --gpu
    ffmpeg -framerate 30 -i /tmp/teaser-frames/%05d.png -c:v libx264 -pix_fmt yuv420p \
           -crf 27 -preset slow -movflags +faststart docs/apollo11_teaser.mp4

Reads landing.csv and landing.events.csv of a complete run from the project directory.
``--gpu`` uses the full Chromium with GPU flags (about 0.3 s per frame on an RTX 2080);
without it the software renderer takes about 3 s per frame.  ``--from/--to`` split the
3690 frames over several processes.  The page and its data are served to the browser
from memory via Playwright routing, so no server is started and no window opens.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument("project")
ap.add_argument("out")
ap.add_argument("--fps", type=int, default=30)
ap.add_argument("--width", type=int, default=1280)
ap.add_argument("--height", type=int, default=720)
ap.add_argument("--limit", type=int, default=0, help="render only the first N frames (smoke test)")
ap.add_argument("--every", type=int, default=1, help="render every k-th frame (smoke test)")
ap.add_argument("--from", dest="frm", type=int, default=0)
ap.add_argument("--to", type=int, default=0, help="exclusive frame index")
ap.add_argument("--gpu", action="store_true", help="full Chromium with GPU flags instead of the software renderer")
ap.add_argument("--headed", action="store_true", help="open a real window on $DISPLAY (uses the GPU)")
args = ap.parse_args()

sys.path.insert(0, args.project)
from agc.sim.viewer import HTML, read_events, read_telemetry  # noqa: E402

proj = Path(args.project)
rows = read_telemetry(proj / "landing.csv")
events = read_events(proj / "landing.events.csv")
if not rows:
    sys.exit("no telemetry")
T0 = rows[0]["t"]
T_END = rows[-1]["t"]
print(f"{len(rows)} rows, t {T0:.1f} .. {T_END:.1f} s, {len(events)} events")


def ev_time(pattern: str, default: float) -> float:
    for e in events:
        if pattern.lower() in e["event"].lower():
            return e["t"]
    return default


# ---- mission milestones (simulated seconds since scenario start) ------------------
t_p63 = ev_time("PROG 63", 1.7)
t_tig_known = ev_time("AGC computed TIG", 17)
t_r60_done = ev_time("maneuver complete", 40)
t_ign = ev_time("DPS ignition", 455)
t_lr = ev_time("LR range data good", 821)
t_v57 = ev_time("V57E", 829)
t_p64 = ev_time("PROG 64", 962)
t_p65 = ev_time("PROG 65", 1127)
t_contact = ev_time("CONTACT", T_END)
t_contact = min(t_contact, T_END)
print(f"milestones: ign {t_ign:.1f} lr {t_lr:.1f} p64 {t_p64:.1f} p65 {t_p65:.1f} contact {t_contact:.1f}")

# ---- video script: (sim_from, sim_to, video_seconds, camera, caption) -------------
# A segment with sim_from == sim_to is a hold.
C = {
    "title1": "Apollo 11 - the original 1969 flight software flies the landing again",
    "title2": "Luminary 099, assembled from the listing, executed cycle by cycle in a Python AGC emulator, "
              "steering a simulated Lunar Module.  No guidance algorithm was rewritten.",
    "p63": "The crew keys V37E63E.  P63 computes the ignition time itself and turns the LM to burn attitude (R60).",
    "coast": "Coasting to the computed ignition time.  The computer waits, the crew keys V99 to permit ignition.",
    "ign": "DPS ignition at 10 % throttle.  After 26 s Luminary commands full throttle - its own decision.",
    "brake": "P63 braking phase: 1,700 m/s of orbital speed to lose.  Throttle and attitude come from the 1969 code.",
    "lr": "Landing radar locked.  V57: the crew lets the computer use it.  The AGC corrects its own altitude estimate.",
    "p64": "High gate, 2.3 km up.  P64 pitches the LM upright, the landing site comes into the window.",
    "p64b": "P64 approach phase.  N64 on the DSKY: the landing point designator angle the crew would look along.",
    "p65": "P65 automatic landing: horizontal velocity nulled, descent at 3 ft/s until the probes touch.",
    "contact": "Contact light.  9 m from the target the 1969 program chose, vertical speed -2.9 ft/s.",
    "outro1": "Everything after the keystrokes is the original code.",
    "outro2": "github.com/jweigend/Apollo11",
}
SEG = [
    # sim_from, sim_to, seconds, camera, caption key, kind
    (T0, T0, 6.0, "chase", "title", "card"),
    (T0, t_r60_done + 15, 10.0, "orbit:0.9:0.25:45:2.2", "p63", "run"),
    (t_r60_done + 15, t_ign - 12, 8.0, "chase", "coast", "run"),
    (t_ign - 12, t_ign + 45, 12.0, "side", "ign", "run"),
    (t_ign + 45, t_lr - 5, 24.0, "orbit:2.6:0.3:45:0.9", "brake", "run"),
    (t_lr - 5, t_p64 - 2, 12.0, "chase", "lr", "run"),
    (t_p64 - 2, t_p64 + 60, 12.0, "side", "p64", "run"),
    (t_p64 + 60, t_p65, 12.0, "orbit:0.5:0.35:40:1.6", "p64b", "run"),
    (t_p65, t_contact, 16.0, "orbit:0.4:0.22:45:1.4", "p65", "run"),
    (t_contact, t_contact, 5.0, "orbit:1.4:0.22:45:1.7", "contact", "hold"),
    (t_contact, t_contact, 6.0, "orbit:1.7:0.22:45:1.9", "outro", "card"),
]
FPS = args.fps
frames: list[tuple[float, str, str, str]] = []   # (sim_t, camera, caption key, kind)
for a, b, secs, cam, key, kind in SEG:
    n = max(1, round(secs * FPS))
    for i in range(n):
        f = i / n
        if cam.startswith("orbit:"):
            _, az0, el, dist, az1 = cam.split(":")
            az = float(az0) + (float(az1) - float(az0)) * f
            frames.append((a + (b - a) * f, f"orbit:{az:.4f}:{el}:{dist}", key, kind))
        else:
            frames.append((a + (b - a) * f, cam, key, kind))
total = len(frames)
print(f"{total} frames = {total / FPS:.1f} s of video")


import bisect  # noqa: E402
ROW_T = [r["t"] for r in rows]


def row_pos(t: float) -> float:
    """Fractional row index for simulated time t."""
    if t <= ROW_T[0]:
        return 0.0
    if t >= ROW_T[-1]:
        return float(len(rows) - 1)
    i = bisect.bisect_right(ROW_T, t) - 1
    a, b = ROW_T[i], ROW_T[i + 1]
    return i + (t - a) / (b - a) if b > a else float(i)


# ---- page instrumentation -----------------------------------------------------------
# Expose a tiny API from inside the viewer's closure and add a caption layer.
HOOK = r"""
window.__v = {
  set(p){ playing = false; live = false; pos = p; const i = Math.floor(pos); if (i !== idx) show(i); placeLM(pos - i); },
  cam(m){ camMode = m; document.getElementById('cam').value = m; },
  orbit(az, el, dist){ camMode = 'free'; orbit.az = az; orbit.el = el; orbit.dist = dist; },
  snap(){ camera.position.set(0,0,0); },          // force the next moveCamera() to snap instead of lerp
  ready(){ return rows.length > 0; },
  frame(){ return new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))); },
};
})();"""
page_html = HTML.replace("\n})();\n</script>", "\n" + HOOK + "\n</script>")
assert "window.__v" in page_html
EXTRA_CSS = """
<style>
  #ctl, #toast, #msg { display:none !important; }
  #cap { position:fixed; left:0; right:0; bottom:28px; margin:0 auto; width:fit-content; max-width:80vw; text-align:center;
         background:rgba(8,10,16,.82); border:1px solid #2a3446; border-radius:10px; padding:12px 22px;
         font-size:21px; line-height:1.35; color:#e8edf5; backdrop-filter:blur(4px); opacity:0; transition:opacity .25s; }
  #cap.on { opacity:1; }
  #cap b { color:#7fd1ff; }
  #card { position:fixed; inset:0; display:none; align-items:center; justify-content:center; flex-direction:column;
          background:rgba(5,6,10,.72); text-align:center; padding:0 10vw; }
  #card.on { display:flex; }
  body.cardmode .panel { opacity:0; }
  #card h1 { font-size:34px; color:#7fd1ff; margin:0 0 18px; font-weight:600; letter-spacing:.5px; }
  #card p { font-size:20px; color:#d7dde8; line-height:1.5; margin:0; max-width:900px; }
  #card .url { margin-top:26px; font-size:24px; color:#ffd27a; }
</style>
<div id="cap"></div>
<div id="card"><h1 id="cardh"></h1><p id="cardp"></p><div class="url" id="cardu"></div></div>
"""
page_html = page_html.replace("</body>", EXTRA_CSS + "</body>")

telemetry_json = json.dumps(rows).encode()
events_json = json.dumps(events).encode()

out = Path(args.out)
out.mkdir(parents=True, exist_ok=True)

with sync_playwright() as pw:
    if args.headed:
        browser = pw.chromium.launch(headless=False, args=["--ignore-gpu-blocklist", "--window-size=%d,%d" % (args.width, args.height + 80)])
    elif args.gpu:
        browser = pw.chromium.launch(channel="chromium", args=["--ignore-gpu-blocklist", "--enable-gpu-rasterization",
                                                                "--use-gl=angle", "--use-angle=gl", "--enable-webgl"])
    else:
        browser = pw.chromium.launch(args=["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"])
    page = browser.new_page(viewport={"width": args.width, "height": args.height}, device_scale_factor=1)

    def route(r):
        url = r.request.url
        if url.endswith("/telemetry.json"):
            r.fulfill(status=200, content_type="application/json", body=telemetry_json)
        elif url.endswith("/events.json"):
            r.fulfill(status=200, content_type="application/json", body=events_json)
        else:
            r.fulfill(status=200, content_type="text/html; charset=utf-8", body=page_html)

    page.route("http://teaser.local/**", route)
    page.goto("http://teaser.local/")
    for _ in range(100):
        if page.evaluate("window.__v && window.__v.ready()"):
            break
        time.sleep(0.1)
    else:
        sys.exit("viewer did not load telemetry")
    page.evaluate("window.__v.cam('chase'); window.__v.set(0); window.__v.snap();")
    page.evaluate("window.__v.frame()")

    last_cam = None
    last_cap = None
    t_wall = time.time()
    done = 0
    for n, (t, cam, key, kind) in enumerate(frames):
        if args.limit and n >= args.limit * args.every:
            break
        if n % args.every or n < args.frm or (args.to and n >= args.to):
            continue
        if cam != last_cam:
            if cam.startswith("orbit:"):
                _, az, el, dist = cam.split(":")
                snap = "window.__v.snap();" if not (last_cam or "").startswith("orbit:") else ""
                page.evaluate(f"window.__v.orbit({az}, {el}, {dist}); {snap}")
            else:
                page.evaluate(f"window.__v.cam({cam!r}); window.__v.snap();")
            last_cam = cam
        page.evaluate(f"window.__v.set({row_pos(t)})")
        # captions / cards
        if kind == "card":
            if key == "title":
                js = f"cardh.textContent={C['title1']!r}; cardp.textContent={C['title2']!r}; cardu.textContent=''; card.classList.add('on'); document.body.classList.add('cardmode'); cap.classList.remove('on');"
            else:
                js = f"cardh.textContent={C['outro1']!r}; cardp.textContent=''; cardu.textContent={C['outro2']!r}; card.classList.add('on'); document.body.classList.add('cardmode'); cap.classList.remove('on');"
            page.evaluate(js)
            last_cap = key
        else:
            if key != last_cap:
                page.evaluate(f"card.classList.remove('on'); document.body.classList.remove('cardmode'); cap.textContent={C[key]!r}; cap.classList.add('on');")
                last_cap = key
        page.evaluate("window.__v.frame()")
        page.screenshot(path=str(out / f"{n:05d}.png"))
        done += 1
        if done % 100 == 0 or done == 10:
            el = time.time() - t_wall
            print(f"  {done} frames, {el:.0f} s, {el / done * 1000:.0f} ms/frame", flush=True)
    browser.close()
print(f"wrote {done} frames to {out}")
