#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zz'

from engine import *
import numpy as np

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
MC = 12
MK = 13
MR = 14
MH = 15
ME = 16
TCK = 17
THE = 18
GACK = 19
GAKR = 20
GARH = 21
GAHE = 22

ROWV = 22
ROWD = 16
COL = 37

# adiabatic pt model
eps = 1 # err in temperature
max_iteration = 20
ninc = 360
step = ninc/36
dtheta = 2.0*pi/ninc

# initial conditions
y(THE) = th
y(TCK) = tk
y(TE) = th
y(TC) = tk
iter = 0
terror = 10*eps


