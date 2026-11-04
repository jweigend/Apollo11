"""Browser based 3D viewer for the landing telemetry.

``python -m agc.sim view [landing.csv]`` serves a small web page (three.js from
a CDN, everything else inline) on localhost.  The page polls the CSV written by
the simulation, so it can replay a finished run or follow a running one.

Coordinates: the CSV holds the LM position relative to the landing site in an
east/north/up frame.  The page shows the lunar sphere, the landing site, the
flown trajectory, the LM with its true attitude, the DPS plume (length ~ thrust)
and RCS firings, plus a DSKY-like head-up display.
"""

from __future__ import annotations

import csv
import errno
import json
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlsplit

NUMERIC = {"t", "get", "alt_m", "hdot_mps", "vhor_mps", "thrust_n", "mass_kg", "pitch_deg",
           "east_m", "north_m", "up_m", "bx_e", "bx_n", "bx_u", "bz_e", "bz_n", "bz_u",
           "gimbal_pitch_deg", "gimbal_roll_deg"}


def read_telemetry(path: Path) -> list[dict]:
    rows = []
    if not path.exists():
        return rows
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            try:
                out = {}
                for k, v in r.items():
                    if k is None:
                        continue
                    if k in NUMERIC:
                        out[k] = float(v) if v not in ("", None) else 0.0
                    elif k == "jets":
                        out[k] = int(v, 8) if v else 0
                    else:
                        out[k] = v if v is not None else ""
                rows.append(out)
            except ValueError:
                continue        # a partially written last line
    return rows


def read_events(path: Path) -> list[dict]:
    """Event log (t, get, event) written by the simulation next to the telemetry."""
    out = []
    if not path.exists():
        return out
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            try:
                out.append({"t": float(r["t"]), "get": float(r["get"]), "event": r["event"]})
            except (ValueError, KeyError, TypeError):
                continue
    return out


HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Eagle Descent</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root { --bg:#05060a; --fg:#d7dde8; --dim:#7b8494; --acc:#7fd1ff; --warn:#ffb347; --dsky:#7CFF7C; }
  html,body { margin:0; height:100%; background:var(--bg); color:var(--fg); font:13px/1.35 ui-monospace,Menlo,Consolas,monospace; overflow:hidden; }
  #c { position:fixed; inset:0; width:100%; height:100%; display:block; }   /* a canvas keeps 300x150 without explicit size */
  .panel { position:fixed; background:rgba(8,10,16,.78); border:1px solid #1e2634; border-radius:8px; padding:10px 12px; backdrop-filter: blur(4px); }
  #hud { left:12px; top:12px; min-width:300px; }
  #dsky { right:12px; top:12px; width:250px; }
  #ctl { left:12px; bottom:12px; right:12px; display:flex; gap:10px; align-items:center; flex-wrap:wrap; }
  #ctl input[type=range] { flex:1; min-width:200px; }
  button, select { background:#141a26; color:var(--fg); border:1px solid #2a3446; border-radius:6px; padding:4px 10px; font:inherit; cursor:pointer; }
  button:hover { border-color:var(--acc); }
  .k { color:var(--dim); } .v { color:var(--fg); }
  .row { display:flex; justify-content:space-between; gap:12px; }
  .dsky-digits { color:var(--dsky); font-size:20px; letter-spacing:2px; text-shadow:0 0 6px rgba(124,255,124,.6); }
  .lamp { display:inline-block; padding:1px 6px; margin:2px 2px 0 0; border-radius:3px; background:#1a1f2a; color:#3a4150; font-size:11px; }
  .lamp.on { background:#f2b63a; color:#1a1200; }
  .warn { color:var(--warn); }
  #title { font-weight:600; color:var(--acc); margin-bottom:6px; }
  #msg { position:fixed; left:50%; top:12px; transform:translateX(-50%); color:var(--warn); }
  #log { right:12px; top:196px; width:360px; max-height:44vh; overflow:hidden; font-size:12px; }
  #log .title { color:var(--acc); font-weight:600; margin-bottom:4px; }
  .ev { display:flex; gap:8px; line-height:1.3; margin:1px 0; }
  .ev .t { color:var(--dim); flex:0 0 78px; }
  .ev .m { color:var(--dim); }
  .ev.crew .m { color:#f2b63a; }
  .ev.agc .m { color:var(--dsky); }
  .ev.dsky .m { color:var(--fg); }
  .ev.alarm .m { color:#ff6b6b; }
  .ev:last-child .m { color:var(--fg); } .ev.crew:last-child .m { color:#ffd27a; }
  #toast { position:fixed; left:50%; top:46px; transform:translateX(-50%); background:rgba(8,10,16,.88); border:1px solid #f2b63a;
           color:#ffd27a; padding:8px 18px; border-radius:8px; font-size:16px; opacity:0; transition:opacity .35s; pointer-events:none; max-width:70vw; }
  #toast.on { opacity:1; }
  #toast .who { color:var(--dim); font-size:12px; margin-right:8px; }
</style>
</head>
<body>
<canvas id="c"></canvas>
<div id="hud" class="panel">
  <div id="title">Apollo 11 - Eagle powered descent (Luminary 099 in the loop)</div>
  <div class="row"><span class="k">GET</span><span class="v" id="get">-</span></div>
  <div class="row"><span class="k">altitude</span><span class="v" id="alt">-</span></div>
  <div class="row"><span class="k">descent rate</span><span class="v" id="hdot">-</span></div>
  <div class="row"><span class="k">ground speed</span><span class="v" id="vh">-</span></div>
  <div class="row"><span class="k">range to site</span><span class="v" id="rng">-</span></div>
  <div class="row"><span class="k">DPS thrust</span><span class="v" id="thr">-</span></div>
  <div class="row"><span class="k">mass</span><span class="v" id="mass">-</span></div>
  <div class="row"><span class="k">pitch from vertical</span><span class="v" id="pitch">-</span></div>
  <div class="row"><span class="k">trim gimbal</span><span class="v" id="gmb">-</span></div>
  <div class="row"><span class="k">landing radar</span><span class="v" id="lr">-</span></div>
  <div class="row"><span class="k">RCS jets</span><span class="v" id="jets">-</span></div>
  <div class="row"><span class="k">alarms</span><span class="v warn" id="alarms">-</span></div>
</div>
<div id="dsky" class="panel">
  <div class="row"><span class="k">PROG</span><span class="dsky-digits" id="prog">  </span></div>
  <div class="row"><span class="k">VERB / NOUN</span><span class="dsky-digits" id="vn">  /  </span></div>
  <div class="row"><span class="k">R1</span><span class="dsky-digits" id="r1"></span></div>
  <div class="row"><span class="k">R2</span><span class="dsky-digits" id="r2"></span></div>
  <div class="row"><span class="k">R3</span><span class="dsky-digits" id="r3"></span></div>
  <div style="margin-top:6px"><span class="lamp" id="l-prog">PROG</span><span class="lamp" id="l-alt">ALT</span><span class="lamp" id="l-vel">VEL</span><span class="lamp" id="l-eng">ENGINE</span></div>
</div>
<div id="ctl" class="panel">
  <button id="play">Pause</button>
  <button id="live">Live</button>
  <label>speed <select id="speed"><option>0.25</option><option>0.5</option><option selected>1</option><option>2</option><option>5</option><option>10</option></select></label>
  <label>camera <select id="cam"><option value="chase" selected>chase</option><option value="side">side</option><option value="site">landing site</option><option value="free">free (drag)</option></select></label>
  <label><input type="checkbox" id="truescale"> true LM size</label>
  <input type="range" id="slider" min="0" max="0" step="1" value="0">
  <span id="tlabel" class="k">-</span>
</div>
<div id="log" class="panel"><div class="title">crew &amp; AGC log</div><div id="logbody"><span class="k">no events yet</span></div></div>
<div id="toast"></div>
<div id="msg"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
(() => {
const R_MOON = 1735.016;                  // km, landing-site radius
const FT = 0.3048;
// A recorded flight starts as a replay.  The simulator opens this page with
// ?live=1 so a growing CSV is followed without manual interaction.
const requestedLive = new URLSearchParams(window.location.search).get('live') === '1';
let rows = [], idx = 0, pos = 0, playing = true, live = requestedLive, lastFetch = 0, speed = 1;
// idx: telemetry row shown in the HUD; pos: fractional row index used to place the LM and the
// camera every frame, so the picture moves smoothly instead of jumping once per sample.
let camMode = 'chase', trueScale = false;
let events = [], evShown = -1, toastTimer = 0;
const esc = s => s.replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
function classify(m){
  if (m.startsWith('crew:')) return ['crew', m.slice(5).trim()];
  if (/^PROG |^DPS ignition|^AGC computed|^\*\*\*|^contact at|^LR |^throttle/i.test(m)) return ['agc', m];
  if (/alarm/i.test(m)) return ['alarm', m];
  if (m.startsWith('DSKY')) return ['dsky', m];
  return ['sys', m]; }
function toast(cls, text){ const el = document.getElementById('toast');
  el.innerHTML = `<span class="who">${cls === 'crew' ? 'CREW' : 'AGC'}</span>${esc(text)}`; el.classList.add('on');
  clearTimeout(toastTimer); toastTimer = setTimeout(() => el.classList.remove('on'), 5000); }
// Show the events up to mission time `get`; announce new crew / program events while moving forward.
function renderLog(get){
  if (!events.length || !rows.length) return;
  const vis = events.filter(e => e.get <= get + 1e-6 && e.get >= rows[0].get - 0.5);
  const n = vis.length;
  document.getElementById('logbody').innerHTML = vis.slice(-14).map(e => { const [c, m] = classify(e.event);
    return `<div class="ev ${c}"><span class="t">${fmtGET(e.get)}</span><span class="m">${esc(m)}</span></div>`; }).join('') || '<span class="k">-</span>';
  if (evShown < 0 || n < evShown){ evShown = n; return; }          // first render or jump back: no announcements
  if (n > evShown){ const fresh = vis.slice(evShown).map(e => classify(e.event)).filter(([c]) => c === 'crew' || c === 'agc' || c === 'alarm');
    if (fresh.length){ const [c, m] = fresh[fresh.length-1]; toast(c, m); } }
  evShown = n; }

// ---- renderer / scene ------------------------------------------------------
const canvas = document.getElementById('c');
const renderer = new THREE.WebGLRenderer({canvas, antialias:true, logarithmicDepthBuffer:true});
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x05060a);
const camera = new THREE.PerspectiveCamera(50, 1, 0.5, 5e6);
// Sun low in the east (Apollo 11 landed at ~11 deg sun elevation, approaching from the east)
const sun = new THREE.DirectionalLight(0xfff2dd, 1.25); sun.position.set(0.95, 0.2, 0.25); scene.add(sun);
scene.add(new THREE.AmbientLight(0x404a5a, 0.55));
// stars
{ const g = new THREE.BufferGeometry(); const n = 3000; const a = new Float32Array(n*3);
  for (let i=0;i<n;i++){ // uniform random direction (Vector3.randomDirection needs three.js >= r129)
    const u = Math.random()*2-1, ph = Math.random()*2*Math.PI, s = Math.sqrt(1-u*u);
    a.set([s*Math.cos(ph)*4e6, u*4e6, s*Math.sin(ph)*4e6], i*3); }
  g.setAttribute('position', new THREE.BufferAttribute(a,3));
  scene.add(new THREE.Points(g, new THREE.PointsMaterial({color:0xffffff, size:3, sizeAttenuation:false}))); }

// Moon: sphere centred below the landing site.  ENU (e,n,u) -> three (x=e, y=u, z=-n), in km.
// Procedural regolith: mottled grey with craters (dark floor, bright rim).  The same canvas
// serves as bump map, so the craters catch the low sun.
function craterCanvas(w, h, n, rmin, rmax, seed, rocks = 0, noise = 30){
  const c = document.createElement('canvas'); c.width = w; c.height = h; const g = c.getContext('2d');
  let sd = seed; const rnd = () => (sd = (sd * 16807) % 2147483647) / 2147483647;
  const img = g.createImageData(w, h), d = img.data;
  for (let i = 0; i < d.length; i += 4){ const v = 138 + (rnd() - 0.5) * noise; d[i] = d[i+1] = d[i+2] = v; d[i+3] = 255; }
  g.putImageData(img, 0, 0);
  for (let k = 0; k < n; k++){
    const r = rmin + (rmax - rmin) * Math.pow(rnd(), 3), x = rnd() * w, y = rnd() * h, dk = 0.35 + rnd() * 0.3;
    const gr = g.createRadialGradient(x, y, 0, x, y, r);
    gr.addColorStop(0, `rgba(55,55,55,${dk})`); gr.addColorStop(0.72, `rgba(75,75,75,${dk * 0.7})`);
    gr.addColorStop(0.86, 'rgba(215,215,215,0.55)'); gr.addColorStop(1, 'rgba(140,140,140,0)');
    g.fillStyle = gr; g.beginPath(); g.arc(x, y, r, 0, 2 * Math.PI); g.fill(); }
  // soft large-scale shading (maria / highlands)
  for (let k = 0; k < 14; k++){ const r = (0.08 + rnd() * 0.25) * w, x = rnd() * w, y = rnd() * h;
    const gr = g.createRadialGradient(x, y, 0, x, y, r); const v = rnd() < 0.5 ? '40,40,45' : '190,190,185';
    gr.addColorStop(0, `rgba(${v},0.18)`); gr.addColorStop(1, `rgba(${v},0)`); g.fillStyle = gr; g.fillRect(x - r, y - r, 2 * r, 2 * r); }
  for (let k = 0; k < rocks; k++){ const r = 1 + rnd() * 2.5, x = rnd() * w, y = rnd() * h;   // boulders: lit side + shadow
    g.fillStyle = 'rgba(40,40,40,0.8)'; g.beginPath(); g.ellipse(x - r * 1.2, y, r * 1.6, r * 0.8, 0, 0, 2 * Math.PI); g.fill();
    g.fillStyle = 'rgba(205,205,205,0.9)'; g.beginPath(); g.arc(x, y, r, 0, 2 * Math.PI); g.fill(); }
  return c; }
function canvasTexture(c, repeat){ const t = new THREE.CanvasTexture(c); t.wrapS = t.wrapT = THREE.RepeatWrapping;
  t.repeat.set(repeat, repeat); t.anisotropy = Math.min(8, renderer.capabilities.getMaxAnisotropy()); return t; }
const moonCanvas = craterCanvas(2048, 1024, 900, 2, 60, 12345);
const moonTex = canvasTexture(moonCanvas, 1), moonBump = canvasTexture(moonCanvas, 1);
const moonMat = new THREE.MeshStandardMaterial({color:0xa8a8a8, map:moonTex, bumpMap:moonBump, bumpScale:4.0, roughness:1.0, metalness:0.0});
const moon = new THREE.Mesh(new THREE.SphereGeometry(R_MOON, 256, 128), moonMat);
moon.position.set(0, -R_MOON, 0); moon.rotation.x = Math.PI / 2;      // texture poles away from the landing site
scene.add(moon);
// high-resolution patch (30 km across, ~15 m/px) around the landing site for the final approach
{ const patchCanvas = craterCanvas(2048, 2048, 2600, 2, 70, 777, 0, 18);
  const patchTex = canvasTexture(patchCanvas, 1), patchBump = canvasTexture(patchCanvas, 1);
  const patch = new THREE.Mesh(new THREE.CircleGeometry(15, 96),
      new THREE.MeshStandardMaterial({color:0xa8a8a8, map:patchTex, bumpMap:patchBump, bumpScale:0.05, roughness:1.0, metalness:0.0, transparent:true, opacity:1}));
  patch.rotation.x = -Math.PI / 2; patch.position.y = 0.0003; scene.add(patch);
  // fine patch (2 km across, ~1 m/px) with small craters and boulders for the final hundred metres
  const fineCanvas = craterCanvas(2048, 2048, 1800, 2, 40, 4242, 900, 6);
  const fineTex = canvasTexture(fineCanvas, 1), fineBump = canvasTexture(fineCanvas, 1);
  window.fine = new THREE.Mesh(new THREE.CircleGeometry(1.0, 64),
      new THREE.MeshStandardMaterial({color:0xa8a8a8, map:fineTex, bumpMap:fineBump, bumpScale:0.004, roughness:1.0, metalness:0.0}));
  fine.rotation.x = -Math.PI / 2; fine.position.y = 0.0005; scene.add(fine);
  // The fine patch follows the LM's ground position; the texture is offset by the same amount so
  // that the pattern stays fixed in the world (the circle spans 2 km = one texture repeat).
  window.placeFine = (x, z) => { fine.position.x = x; fine.position.z = z;
    fineTex.offset.set(x / 2, -z / 2); fineBump.offset.set(x / 2, -z / 2); }; }
// grid on the surface near the site (10 km squares out to 500 km), draped on the sphere
{ const pts = [];
  for (let k=-50;k<=50;k++){ const s=k*10; for (let m=-50;m<50;m++){ const a=m*10, b=(m+1)*10;
      pts.push(...onSphere(s,a), ...onSphere(s,b)); pts.push(...onSphere(a,s), ...onSphere(b,s)); } }
  const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.Float32BufferAttribute(pts,3));
  scene.add(new THREE.LineSegments(g, new THREE.LineBasicMaterial({color:0x2c3442, transparent:true, opacity:0.3}))); }
function onSphere(e, n){ // point on the sphere surface (km) at ENU ground offsets, slightly above
  const d = Math.hypot(e, n); const ang = d / R_MOON; const r = R_MOON + 0.02;
  const up = Math.cos(ang) * r - R_MOON; const horiz = Math.sin(ang) * r; const f = d > 0 ? horiz / d : 0;
  return [e*f, up, -n*f]; }
// landing site marker
{ const ring = new THREE.Mesh(new THREE.RingGeometry(0.002, 0.0028, 48), new THREE.MeshBasicMaterial({color:0xff5a5a, side:THREE.DoubleSide, transparent:true, opacity:0.7}));
  ring.rotation.x = -Math.PI/2; ring.position.y = 0.0008; scene.add(ring);
  const ring2 = new THREE.Mesh(new THREE.RingGeometry(0.9, 1.0, 64), new THREE.MeshBasicMaterial({color:0xff5a5a, side:THREE.DoubleSide, transparent:true, opacity:0.4}));
  ring2.rotation.x = -Math.PI/2; ring2.position.y = 0.0008; scene.add(ring2);
  // a thin 12 m mast at the target (the LM sets down right next to it)
  const pole = new THREE.Mesh(new THREE.CylinderGeometry(0.00012,0.00012,0.012,8), new THREE.MeshBasicMaterial({color:0xff5a5a})); pole.position.y=0.006; scene.add(pole); }

// trajectory
const trajGeo = new THREE.BufferGeometry(); const trajMax = 5000;
trajGeo.setAttribute('position', new THREE.BufferAttribute(new Float32Array(trajMax*3), 3)); trajGeo.setDrawRange(0,0);
scene.add(new THREE.Line(trajGeo, new THREE.LineBasicMaterial({color:0x7fd1ff})));
const trackGeo = new THREE.BufferGeometry();
trackGeo.setAttribute('position', new THREE.BufferAttribute(new Float32Array(trajMax*3), 3)); trackGeo.setDrawRange(0,0);
scene.add(new THREE.Line(trackGeo, new THREE.LineBasicMaterial({color:0x3b5d78})));

// LM model (units: metres, built with body +X = model +Y, body +Z = model +Z, body +Y = model -X ... handled by basis)
const lm = new THREE.Group();
// The simulation's altitude is that of the centre of mass; the model hangs 3.35 m below it
// (footpads), so lift the body by that amount and the pads touch down at altitude 0.
const body = new THREE.Group(); body.position.y = 3.35; lm.add(body);
{ const gold = new THREE.MeshStandardMaterial({color:0xc9a227, metalness:0.6, roughness:0.4});
  const grey = new THREE.MeshStandardMaterial({color:0xa9adb5, metalness:0.15, roughness:0.75});
  const dark = new THREE.MeshStandardMaterial({color:0x33363c, roughness:0.8});
  const desc = new THREE.Mesh(new THREE.CylinderGeometry(2.1, 2.1, 1.65, 8), gold); desc.position.y = -0.8; body.add(desc);
  const asc = new THREE.Mesh(new THREE.SphereGeometry(1.4, 16, 12), grey); asc.position.y = 1.0; asc.scale.set(1,0.9,1.25); body.add(asc);
  const hatch = new THREE.Mesh(new THREE.BoxGeometry(0.8,0.8,0.5), dark); hatch.position.set(0,0.9,1.6); body.add(hatch);
  for (let i=0;i<4;i++){ const a = Math.PI/4 + i*Math.PI/2;
    const leg = new THREE.Mesh(new THREE.CylinderGeometry(0.06,0.06,3.0,6), grey);
    leg.position.set(Math.cos(a)*2.6, -2.0, Math.sin(a)*2.6); leg.rotation.z = Math.cos(a)*0.55; leg.rotation.x = -Math.sin(a)*0.55; body.add(leg);
    const pad = new THREE.Mesh(new THREE.CylinderGeometry(0.45,0.45,0.1,10), grey); pad.position.set(Math.cos(a)*3.4, -3.35, Math.sin(a)*3.4); body.add(pad);
    // RCS quads at 45 deg positions, slightly above the CG
    const quad = new THREE.Mesh(new THREE.BoxGeometry(0.4,0.4,0.4), dark); quad.position.set(Math.cos(a)*1.65, 0.75, Math.sin(a)*1.65); body.add(quad); }
  const bell = new THREE.Mesh(new THREE.ConeGeometry(0.75, 1.2, 16, 1, true), dark); bell.position.y = -2.1; bell.rotation.x = Math.PI; body.add(bell);
  window.plume = new THREE.Mesh(new THREE.ConeGeometry(0.6, 1, 16, 1, true),
      new THREE.MeshBasicMaterial({color:0xffa040, transparent:true, opacity:0.75, side:THREE.DoubleSide}));
  plume.rotation.x = Math.PI; plume.position.y = -3.3; plume.visible = false; body.add(plume);
  window.puffs = [];
  for (let i=0;i<16;i++){ const p = new THREE.Mesh(new THREE.SphereGeometry(0.25, 8, 6), new THREE.MeshBasicMaterial({color:0xfff0c0, transparent:true, opacity:0.9}));
    p.visible = false; body.add(p); puffs.push(p); } }
scene.add(lm);
// jet geometry (body frame, metres): quads 1 front-left(+Z,-Y) 2 aft-left 3 aft-right 4 front-right; force directions
const A = 1.65/Math.SQRT2;
const QUAD = {1:[0.75,-A, A], 2:[0.75,-A,-A], 3:[0.75, A,-A], 4:[0.75, A, A]};
const DIR = {U:[-1,0,0], D:[1,0,0], F:[0,0,-1], A:[0,0,1], L:[0,1,0], R:[0,-1,0]};
const JETS = ["B4U","A4D","A3U","B3D","B2U","A2D","A1U","B1D", "B3A","B4F","A1F","A2A","B2L","A3R","A4R","B1L"];

// ---- helpers ------------------------------------------------------------------
const toScene = (e,n,u) => new THREE.Vector3(e/1000, u/1000, -n/1000);   // metres ENU -> km scene
function bodyToScene(v){ return new THREE.Vector3(v[0], v[2], -v[1]); }     // ENU components -> scene axes
function setAttitude(row){
  const bx = bodyToScene([row.bx_e,row.bx_n,row.bx_u]).normalize();          // body +X (thrust axis) -> model +Y
  const bz = bodyToScene([row.bz_e,row.bz_n,row.bz_u]).normalize();          // body +Z (windows)     -> model +Z
  const by = new THREE.Vector3().crossVectors(bz, bx).normalize();           // body +Y = Z x X        -> model -X
  const m = new THREE.Matrix4().makeBasis(by.clone().negate(), bx, bz);
  lm.quaternion.setFromRotationMatrix(m); }
const f1 = (x,d=1) => (x===undefined||isNaN(x)) ? '-' : x.toFixed(d);
function fmtGET(s){ const h=Math.floor(s/3600), m=Math.floor((s%3600)/60), sec=s%60; return `${String(h).padStart(3,'0')}:${String(m).padStart(2,'0')}:${sec.toFixed(1).padStart(4,'0')}`; }

// ---- camera control (free mode) -----------------------------------------------------
let orbit = {az: 0.6, el: 0.35, dist: 60}; let drag=null;
// Smooth camera motion, but snap on the first frame and on big jumps (slider, start of a
// replay 1000+ km from the site): lerping in from the origin would put the camera inside the
// moon sphere for several seconds and show only a black screen.
function moveCamera(target, sz){
  if (camera.position.distanceTo(target) > sz*40) camera.position.copy(target); else camera.position.lerp(target, 0.15); }
canvas.addEventListener('mousedown', e => { drag = {x:e.clientX, y:e.clientY}; if (camMode!=='free'){ document.getElementById('cam').value='free'; camMode='free'; } });
window.addEventListener('mouseup', () => drag=null);
window.addEventListener('mousemove', e => { if(!drag) return; orbit.az -= (e.clientX-drag.x)*0.005; orbit.el = Math.max(-1.4, Math.min(1.5, orbit.el + (e.clientY-drag.y)*0.005)); drag={x:e.clientX,y:e.clientY}; });
canvas.addEventListener('wheel', e => { orbit.dist *= Math.exp(e.deltaY*0.001); orbit.dist = Math.max(0.01, Math.min(3000, orbit.dist)); }, {passive:true});

// Local vertical at a scene point: radial from the moon's centre.  At PDI the LM is ~1150 km from the
// landing site, where the site's 'up' (scene +Y) is tilted ~38 deg from the real vertical.
function localUp(p){ return p.clone().sub(moon.position).normalize(); }
function updateCamera(row){
  const p = toScene(row.east_m, row.north_m, row.up_m);
  const up = localUp(p);
  const fwd = (window.lastDir||new THREE.Vector3(1,0,0)).clone(); fwd.sub(up.clone().multiplyScalar(fwd.dot(up))).normalize();   // heading in the local tangent plane
  const altKm = Math.max(row.alt_m/1000, 0.002);
  const scale = trueScale ? 0.001 : Math.max(0.001, altKm/150);     // model metres -> km, enlarged when far away
  lm.scale.setScalar(scale);
  const sz = 8*scale;                                                   // visual LM size (km)
  if (camMode === 'chase'){                                             // behind and above, looking along the flight path
    const back = fwd.clone().multiplyScalar(-1);
    const camPos = p.clone().add(back.multiplyScalar(sz*4.5)).add(up.clone().multiplyScalar(sz*1.8));
    moveCamera(camPos, sz); camera.up.copy(up); camera.lookAt(p);
  } else if (camMode === 'side'){
    const side = new THREE.Vector3().crossVectors(fwd, up).normalize();
    const camPos = p.clone().add(side.multiplyScalar(sz*5)).add(up.clone().multiplyScalar(sz*0.8));
    moveCamera(camPos, sz); camera.up.copy(up); camera.lookAt(p);
  } else if (camMode === 'site'){
    camera.position.set(0.3, 0.05, 0.3); camera.up.set(0,1,0); camera.lookAt(p);
  } else {                                                              // orbit in the LM's local frame
    const right = new THREE.Vector3().crossVectors(fwd, up).normalize();
    const off = fwd.clone().multiplyScalar(Math.cos(orbit.el)*Math.cos(orbit.az))
      .add(right.multiplyScalar(Math.cos(orbit.el)*Math.sin(orbit.az)))
      .add(up.clone().multiplyScalar(Math.sin(orbit.el)))
      .multiplyScalar(Math.max(orbit.dist*scale, sz*1.5));
    camera.position.copy(p).add(off); camera.up.copy(up); camera.lookAt(p);
  }
  camera.near = Math.max(0.0005, sz*0.05); camera.updateProjectionMatrix();
}

// ---- update from a telemetry row -----------------------------------------------------
function show(i){
  if (!rows.length) return;
  idx = Math.max(0, Math.min(rows.length-1, i));
  const row = rows[idx];
  const p = toScene(row.east_m, row.north_m, row.up_m);
  if (rows.length > 1){ const q = idx > 0 ? rows[idx-1] : rows[1];                  // heading: from the previous (or next) sample
    const d = idx > 0 ? p.clone().sub(toScene(q.east_m,q.north_m,q.up_m)) : toScene(q.east_m,q.north_m,q.up_m).sub(p); const up = localUp(p);
    d.sub(up.multiplyScalar(d.dot(up)));                                   // horizontal part in the LM's own tangent plane
    if (d.length()>1e-6) window.lastDir = d.normalize(); }
  // plume
  const thr = row.thrust_n/43900;
  plume.visible = thr > 0.02; plume.scale.set(0.6+thr*0.8, 1+thr*6, 0.6+thr*0.8); plume.position.y = -3.3 - (plume.scale.y-1)*0.5;
  plume.material.opacity = 0.35 + 0.5*thr;
  // RCS puffs
  for (let j=0;j<16;j++){ const on = (row.jets>>j)&1; const pf = puffs[j]; pf.visible = !!on; if (on){ const name=JETS[j]; const q=QUAD[+name[1]]; const d=DIR[name[2]];
      // puff sits outside the quad in the exhaust direction (opposite to force)
      pf.position.set(-(q[1]-d[1]*0.6), q[0]-d[0]*0.6, q[2]-d[2]*0.6); } }
  // trajectory arrays
  const tp = trajGeo.attributes.position.array, gp = trackGeo.attributes.position.array; const n = Math.min(idx+1, trajMax);
  for (let k=0;k<n;k++){ const r=rows[k]; const v=toScene(r.east_m,r.north_m,r.up_m); tp.set([v.x,v.y,v.z], k*3);
     const g=onSphere(r.east_m/1000, r.north_m/1000); gp.set(g, k*3); }
  trajGeo.setDrawRange(0,n); trajGeo.attributes.position.needsUpdate = true; trackGeo.setDrawRange(0,n); trackGeo.attributes.position.needsUpdate = true;
  // HUD
  const el = id => document.getElementById(id);
  el('get').textContent = fmtGET(row.get);
  el('alt').textContent = `${f1(row.alt_m/FT,0)} ft  (${f1(row.alt_m,0)} m)`;
  el('hdot').textContent = `${f1(row.hdot_mps/FT,1)} ft/s`;
  el('vh').textContent = `${f1(row.vhor_mps/FT,1)} ft/s  (${f1(row.vhor_mps,1)} m/s)`;
  el('rng').textContent = `${f1(Math.hypot(row.east_m,row.north_m)/1000,2)} km`;
  el('thr').textContent = `${f1(thr*100,1)} %  (${f1(row.thrust_n/1000,1)} kN)`;
  el('mass').textContent = `${f1(row.mass_kg,0)} kg`;
  el('pitch').textContent = `${f1(row.pitch_deg,1)} deg`;
  el('gmb').textContent = `${f1(row.gimbal_pitch_deg,2)} / ${f1(row.gimbal_roll_deg,2)} deg`;
  el('lr').textContent = row.lr ? `${row.lr[0]==='R'?'range ok':'no range'}, ${row.lr[1]==='V'?'velocity ok':'no velocity'}, pos ${row.lr[2]}` : 'off';
  const jets = JETS.filter((_,j)=>(row.jets>>j)&1); el('jets').textContent = jets.length ? jets.join(' ') : 'quiet';
  el('alarms').textContent = row.alarms || 'none';
  el('prog').textContent = row.prog || '  '; el('vn').textContent = `${row.verb||'  '} / ${row.noun||'  '}`;
  el('r1').textContent = row.r1||''; el('r2').textContent = row.r2||''; el('r3').textContent = row.r3||'';
  el('l-prog').classList.toggle('on', !!(row.alarms && row.alarms !== '01107'));
  el('l-alt').classList.toggle('on', !(row.lr && row.lr[0]==='R'));
  el('l-vel').classList.toggle('on', !(row.lr && row.lr[1]==='V'));
  el('l-eng').classList.toggle('on', thr > 0.02);
  el('slider').max = rows.length-1; el('slider').value = idx; el('tlabel').textContent = `${idx+1}/${rows.length}  ${live?'LIVE':''}`;
  renderLog(row.get);
}
// Place the LM (and the camera) at fractional position f between rows[idx] and rows[idx+1].
const LERP_KEYS = ['east_m','north_m','up_m','bx_e','bx_n','bx_u','bz_e','bz_n','bz_u','alt_m','vhor_mps'];
function placeLM(f){
  const a = rows[idx], b = rows[Math.min(idx+1, rows.length-1)];
  let row = a;
  if (f > 0 && b !== a){ row = {...a}; for (const k of LERP_KEYS) row[k] = a[k] + (b[k]-a[k])*f; }
  lm.position.copy(toScene(row.east_m, row.north_m, row.up_m)); setAttitude(row);
  if (Math.hypot(lm.position.x, lm.position.z) < 14) placeFine(lm.position.x, lm.position.z);
  updateCamera(row);
}

// ---- data polling -----------------------------------------------------------------
async function fetchData(){
  try { const ev = await fetch('/events.json', {cache:'no-store'}); const evd = await ev.json();
        if (evd.length !== events.length){ events = evd; if (rows.length) renderLog(rows[idx].get); } } catch(e){}
  try { const r = await fetch('/telemetry.json', {cache:'no-store'}); const d = await r.json();
        if (d.length !== rows.length){ const first = !rows.length; rows = d;
          if (first){ pos = live ? Math.max(0, rows.length-2) : 0; show(Math.floor(pos)); } else if (!live) show(idx); }
        document.getElementById('msg').textContent = rows.length ? '' : 'waiting for telemetry (start: python -m agc.sim land) ...'; }
  catch(e){ document.getElementById('msg').textContent = 'telemetry server not reachable'; }
}
setInterval(fetchData, 1500); fetchData();

// ---- controls -----------------------------------------------------------------------
document.getElementById('play').onclick = () => {
  if (pos >= rows.length-1) { pos = 0; live = false; show(0); }
  playing = !playing;
  document.getElementById('play').textContent = playing ? 'Pause' : 'Play';
};
document.getElementById('live').onclick = () => { live = true; playing = true; pos = Math.max(0, rows.length-2); show(Math.floor(pos)); };
document.getElementById('speed').onchange = e => speed = parseFloat(e.target.value);
document.getElementById('cam').onchange = e => camMode = e.target.value;
document.getElementById('truescale').onchange = e => trueScale = e.target.checked;
document.getElementById('slider').oninput = e => { live = false; pos = parseInt(e.target.value); show(pos); };
let lastT = performance.now();
function animate(now){
  requestAnimationFrame(animate);
  const dt = (now-lastT)/1000; lastT = now;
  if (rows.length){
    const step = rows.length>1 ? (rows[1].t-rows[0].t) : 0.5, last = rows.length-1;
    if (live){                                   // follow the newest sample at mission-time rate
      if (pos < last-6) pos = Math.max(0, last-2); // far behind (new data burst): catch up
      pos = Math.min(last, pos + dt/step);
    } else if (playing){
      pos = Math.min(last, pos + dt*speed/step);
      if (pos >= last){ playing = false; document.getElementById('play').textContent = 'Play'; }
    }
    const i = Math.floor(pos);
    if (i !== idx) show(i);
    placeLM(pos - i);
  }
  const w = canvas.clientWidth||innerWidth, h = canvas.clientHeight||innerHeight;
  if (canvas.width !== w*renderer.getPixelRatio() || canvas.height !== h*renderer.getPixelRatio()){ renderer.setSize(w,h,false); camera.aspect = w/h; camera.updateProjectionMatrix(); }
  renderer.render(scene, camera);
}
requestAnimationFrame(animate);
})();
</script>
</body>
</html>
"""


class _Handler(BaseHTTPRequestHandler):
    csv_path: Path = Path("landing.csv")

    def log_message(self, *args):       # keep the console quiet
        pass

    def do_GET(self):
        path = urlsplit(self.path).path
        if path == "/telemetry.json":
            body = json.dumps(read_telemetry(self.csv_path)).encode()
            ctype = "application/json"
        elif path == "/events.json":
            body = json.dumps(read_events(self.csv_path.with_suffix(".events.csv"))).encode()
            ctype = "application/json"
        elif path in ("/", "/index.html"):
            body = HTML.encode()
            ctype = "text/html; charset=utf-8"
        elif path == "/favicon.ico":
            self.send_response(204)      # browsers ask for it; avoid a 404 in the console
            self.end_headers()
            return
        else:
            self.send_response(404)
            self.end_headers()
            return
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)


def serve(csv_path: str | Path, port: int = 8765, open_browser: bool = True, block: bool = True,
          live: bool = False) -> HTTPServer:
    """Serve the viewer, selecting the next local port if the preferred one is busy."""
    _Handler.csv_path = Path(csv_path)
    httpd = None
    requested_port = port
    for candidate in range(port, port + 20):
        try:
            httpd = HTTPServer(("127.0.0.1", candidate), _Handler)
            port = candidate
            break
        except OSError as exc:
            if exc.errno != errno.EADDRINUSE:
                raise
    if httpd is None:
        raise RuntimeError(f"no free localhost port in range {requested_port}..{requested_port + 19}")
    url = f"http://127.0.0.1:{port}/" + ("?live=1" if live else "")
    suffix = f" (port {requested_port} was busy)" if port != requested_port else ""
    print(f"3D viewer: {url}   (telemetry from {csv_path}, events from {Path(csv_path).with_suffix('.events.csv')}){suffix}")
    print("If the browser runs on another machine, forward this port in your IDE's Ports view.")
    if open_browser:
        try:
            webbrowser.open(url)
        except Exception:
            pass
    if block:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
    else:
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd
