#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zz'

' define the engine parameters '

import numpy as np
pi = np.pi
vswc = 0.0001
vclc = 0.1*vswc
vswe = 0.00005
vcle = 0.1*vswe
vswb = 0.00005
vclb = 0.1*vswb
phi = 30*pi/180
nt = 36
theta = np.linspace(1,nt,nt)*pi/180
p0 = 2*10**6

# cooler
dk = 0.045
lk = 0.004
pork = 0.7
vk = 0.25*pi*dk**2*lk*pork

# heater
dh = 0.045
lh = 0.004
porh = 0.7
vh = 0.25*pi*dh**2*lh*porh

# regenertor
dr = 0.045
lr = 0.07
porr = 0.7
vr = 0.25*pi*dr**2*lr*porr

# pulse tube
dpul = 0.024
lpul = 0.1
vpul = 0.25*pi*dpul**2*lpul

# gas piston
vpon = 1.28
vgclc = vpul*vpon

# gas = helium
gama = 1.67
r = 8.3144598/4
cv = r/(gama-1)
cp = gama*cv
prandtl = 0.6829

# operat
pm = 2*10*6
tk = 300
th = 900
freq = 50

tr = (th - tk)/np.log(th/tk)
omega = 2*pi*freq

