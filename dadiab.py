#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zz'

import numpy as np
from isothermal import *
import volume

def dadiab(theta,y):

# indices of the y, dy vectors
    P = 0
    TC = 1
    TE = 2
    QK = 3
    QR = 4
    QH = 5
    WC = 6
    WE = 7
    WB = 8
    W = 9
    VC = 10
    VE = 11
    VB = 12
    VGE = 13
    MC = 14
    MK = 15
    MR = 16
    MH = 17
    MGE = 18
    MB = 19
    TCK = 20
    THE = 21
    MCK = 22
    MKR = 23
    MRH = 24
    MHGE = 25
    MBC = 26
#-----------------------------------------------
# volume and volume derivatives
    dy = np.zeros((20,37))
    y[VC],y[VE],y[VB],dy[VC],dy[VE],dy[VB] = volume.volume(theta)

# pressure and pressure derivatives
    y[P] = m*r/((y[VC]+y[VB])/y[TC] + vt + y[VGE]/y[TE])
    top = -y[P]*(dy[VC]+dy[VB])/y[TCK] + dy[VE]/y[THE]
    bottom = ((y[VC]+y[VB])/(y[TCK]*gama) + vt + y[VE]/(y[THE]*gama))
    dy[P] = top/bottom

# mass and mass flow
    y[MC] = y[P]*y[VC]/(r*y[TC])
    y[MK] = y[P]*vk/(r*tk)
    y[MR] = y[P]*vr/(r*tr)
    y[MH] = y[P]*vh/(r*th)
    y[MGE] = y[P]*y[VGE]/(r*y[TE])
    dy[MC] = (y[P]*dy[VC]+y[VC]*dy[P]/gama)/(r*y[TCK])
    dy[MGE] = (y[P]*dy[VGE]+y[VE]*dy[P]/gama)/(r*y[THE])
    dpop = dy[P]/y[P]
    dy[MK] = y[MK]*dpop
    dy[MR] = y[MR]*dpop
    dy[MH] = y[MH]*dpop

# mass flow between cells
    y[MBC] = -dy[MB]
    y[MCK] = -dy[MC] - dy[MB]
    y[MHGE] = dy[MGE]
    y[MRH] = dy[MGE] + dy[MH]
    y[MKR] = dy[MR] + dy[MH] + dy[MGE]

# temperature between cells
    y[TCK] = tk
    if(y[MCK].any()>0): y[TCK] = y[TC]
    y[THE] = y[TC]
    if(y[MHGE].any()>0): y[THE] = th

# working space temperature
    dy[TC] = y[TC]*(dpop+dy[VC]/y[VC]-dy[MC]/y[MC])
    dy[TE] = y[TE]*(dpop+dy[VGE]/y[VGE]-dy[MGE]/y[MGE])

# energy
    dy[QK] = vk*dy[P]*cv/r-cp*(y[TCK]*y[MCK]-tk*y[MKR])
    dy[QR] = vr*dy[P]*cv/r-cp*(tk*y[MKR]-th*y[MRH])
    dy[QH] = vh*dy[P]*cv/r-cp*(th*y[MRH]-y[THE]*y[MHGE])
    dy[WC] = y[P]*dy[VC]
    dy[WE] = y[P]*dy[VGE]
    dy[WB] = y[P]*dy[VB]

# net work done
    dy[W] = dy[WC] + dy[WB]
    y[W] = y[WC] + y[WB]

    return y,dy
