/* Reference trace harness around the Virtual AGC engine (yaAGC, GPL).
 *
 * Build (from the repository root):
 *   gcc -O2 -o /tmp/ref_trace tools/ref_trace.c external/virtualagc/yaAGC/{agc_engine.c,agc_engine_init.c,agc_utilities.c,rfopen.c,Backtrace.c,NullAPI.c,DecodeDigitalDownlink.c} -Iexternal/virtualagc/yaAGC -lm
 *
 * Usage: ref_trace Luminary099.bin NCYCLES > trace.txt
 * Prints one line per MCT: cycle Z A L Q EB FB BB InIsr ExtraCode
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "agc_engine.h"

int main(int argc, char **argv)
{
  agc_t state;
  long n, i;
  if (argc < 3) { fprintf(stderr, "usage: ref_trace rope.bin ncycles\n"); return 2; }
  memset(&state, 0, sizeof(state));
  if (agc_engine_init(&state, argv[1], NULL, 0)) { fprintf(stderr, "init failed\n"); return 1; }
  n = atol(argv[2]);
  for (i = 0; i < n; i++)
    {
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
