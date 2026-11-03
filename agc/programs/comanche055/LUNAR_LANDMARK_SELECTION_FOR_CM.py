"""LUNAR_LANDMARK_SELECTION_FOR_CM.agc -- Comanche (build 055), Apollo 11 Command Module guidance computer

Converted from external/Apollo-11/Comanche055/LUNAR_LANDMARK_SELECTION_FOR_CM.agc by agc2py (the Apollo 11 AGC -> Python converter).
Pages 936 of the original program listing.

Every ``W(address, word, label, operator, operand, comment)`` line is one
15-bit word of the AGC rope memory; ``S(name, kind, value)`` defines a symbol.
Original comments are preserved as Python comments.
"""

from agc.program import Module

MODULE = Module('LUNAR_LANDMARK_SELECTION_FOR_CM', 'LUNAR_LANDMARK_SELECTION_FOR_CM.agc', 'Comanche055', pages='936')
W = MODULE.W
S = MODULE.S

# Copyright:    Public domain.
# Filename:     LUNAR_LANDMARK_SELECTION_FOR_CM.agc
# Purpose:      Part of the source code for Colossus 2A, AKA Comanche 055.
# It is part of the source code for the Command Module's (CM)
# Apollo Guidance Computer (AGC), for Apollo 11.
# Assembler:    yaYUL
# Contact:      Jim Lawton <jim.lawton@gmail.com>.
# Website:      www.ibiblio.org/apollo.
# Pages:        936
# Mod history:  2009-05-11 JVL  Adapted from the Colossus249/ file
# of the same name, using Comanche055 page
# images.
#
# This source code has been transcribed or otherwise adapted from digitized
# images of a hardcopy from the MIT Museum.  The digitization was performed
# by Paul Fjeld, and arranged for by Deborah Douglas of the Museum.  Many
# thanks to both.  The images (with suitable reduction in storage size and
# consequent reduction in image quality as well) are available online at
# www.ibiblio.org/apollo.  If for some reason you find that the images are
# illegible, contact me at info@sandroid.org about getting access to the
# (much) higher-quality images which Paul actually created.
#
# Notations on the hardcopy document read, in part:
#
# Assemble revision 055 of AGC program Comanche by NASA
# 2021113-051.  10:28 APR. 1, 1969
#
# This AGC program shall also be referred to as
# Colossus 2A

# Page 936

# *** END OF TROUBLE .043 ***
