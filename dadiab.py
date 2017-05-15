#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zz'

import numpy as np
from isothermal import *

def dadiab(theta,y):

# indices of the y, dy vectors
    TC = 1
	TE = 2
	QK = 3
	QR = 4
	QH = 5
	WC = 6
	WE = 7
	W = 8
	P = 9
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
y[VC],y[VE],y[VB],dy[VC],dy[VE],dy[VB] = volume(theta)

# pressure and pressure derivatives
y[P] = p
top = -y[P]*(dy[VC]/y[TCK] + dy[VE]/y[THE])
bottom = (y[VC]/(y[TCK]*gama) + vt + y[VE]/(y[THE]*gama))
dy[p] = top/bottom

# mass and mass flow
y[MC] = y[P]*y[VC]/(r*y[TC])
y[MK] = y[P]*vk/(r*tk)

