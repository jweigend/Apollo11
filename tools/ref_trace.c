/* Reference trace harness around the Virtual AGC engine (yaAGC, GPL).
 *
 * Build (from the repository root):
 *   gcc -O2 -o /tmp/ref_trace tools/ref_trace.c external/virtualagc/yaAGC/{agc_engine.c,agc_engine_init.c,agc_utilities.c,rfopen.c,Backtrace.c,DecodeDigitalDownlink.c} -Iexternal/virtualagc/yaAGC -lm
 *
 * Usage: ref_trace Luminary099.bin NCYCLES [CYCLE:CHANNEL:VALUE,...] > trace.txt
 * The optional third argument writes input channels (octal) just before the
 * given cycles; a write to channel 15 is a DSKY key and raises KEYRUPT1, e.g.
 * 426665:15:21,447998:15:3,469331:15:5,490664:15:34 keys V35E at 5 s.
 * Prints one line per MCT: cycle Z A L Q EB FB BB InIsr ExtraCode
 *
 * The peripheral interface below replaces yaAGC's NullAPI.c.  NullAPI drops
 * every channel write, including channel 7 (SUPERBNK), which the engine
 * expects its I/O backend to latch into OutputChannel7 (see SocketAPI.c);
 * linked against NullAPI the reference never selects the superbanks 40-43
 * and diverges from the real AGC at the first SUPDXCHZ.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "agc_engine.h"

void ChannelOutput (agc_t *State, int Channel, int Value)
{
  if (Channel == 7)
    State->InputChannel[7] = State->OutputChannel7 = (Value & 0160);
}
int ChannelInput (agc_t *State) { (void) State; return 0; }
void ChannelRoutine (agc_t *State) { (void) State; }
void ShiftToDeda (agc_t *State, int Data) { (void) State; (void) Data; }
void RequestRadarData (agc_t *State) { (void) State; }

int main(int argc, char **argv)
{
  agc_t state;
  long n, i;
  if (argc < 3) { fprintf(stderr, "usage: ref_trace rope.bin ncycles\n"); return 2; }
  memset(&state, 0, sizeof(state));
  if (agc_engine_init(&state, argv[1], NULL, 0)) { fprintf(stderr, "init failed\n"); return 1; }
  n = atol(argv[2]);
  const char *keys = argc > 3 ? argv[3] : "";
  long next_cycle = -1; int next_chan = 0, next_value = 0;
  if (*keys && sscanf(keys, "%ld:%o:%o", &next_cycle, &next_chan, &next_value) != 3) { fprintf(stderr, "bad event list\n"); return 2; }
  for (i = 0; i < n; i++)
    {
      if (i + 1 == next_cycle)
        {
          WriteIO(&state, next_chan, next_value);      /* as SocketAPI does for a channel packet */
          if (next_chan == 015)
            state.InterruptRequests[5] = 1;            /* KEYRUPT1 */
          keys = strchr(keys, ',');
          next_cycle = -1;
          if (keys && sscanf(++keys, "%ld:%o:%o", &next_cycle, &next_chan, &next_value) != 3) { fprintf(stderr, "bad event list\n"); return 2; }
        }
      agc_engine(&state);
      printf("%llu %04o %06o %06o %06o %05o %05o %05o %d %d\n",
             (unsigned long long) state.CycleCounter,
             state.Erasable[0][5] & 07777, state.Erasable[0][0] & 0177777,
             state.Erasable[0][1] & 0177777, state.Erasable[0][2] & 0177777,
             state.Erasable[0][3] & 077777, state.Erasable[0][4] & 077777,
             state.Erasable[0][6] & 077777, state.InIsr, state.ExtraCode);
    }
  return 0;
}
