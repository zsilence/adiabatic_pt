#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zz'

from engine import *
import rk
import dadiab
import filmatrix as fl
import numpy as np

def adiab():

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

    ROWV = 27
    ROWD = 18
    COL = 37

    eps = 1
    max_iteration = 20
    ninc = 360
    step = ninc/36
    dtheta = 2.0*pi/ninc

    #initial conditions
    y = np.zeros((27,37))
    dy = np.zeros((18,37))
    y[THE] = th
    y[TCK] = tk
    y[TE] = th
    y[TC] = tk
    iteration = 0
    terror = 10*eps

    while((terror > eps) & (iteration < max_iteration)):
        tc0 = y[TC]
        te0 = y[TE]
        theta = 0
        y[QK] = 0
        y[QR] = 0
        y[QH] = 0
        y[WC] = 0
        y[WE] = 0
        y[WB] = 0
        for i in range(ninc):
            theta,y,dy = rk.rk4(dadiab.dadiab,7,theta,dtheta,y)
        terror = abs(tc0-y[TC])+abs(te0-y[TE])
        iteration = iteration + 1

    if (iteration >= max_iteration):
        print('No convergence within %d iteration\n',max_iteration)

    var = np.zeros((27,37))
    dvar = np.zeros((18,37))
    theta = 0
    y[QK] = 0
    y[QR] = 0
    y[QH] = 0
    y[WC] = 0
    y[WE] = 0
    y[WB] = 0
    y[W] = 0
    var, dvar = fl.filmatrix(0,y,dy,var,dvar)
    for i in range(1,COL):
        for j in range(step):
            theta,y,dy = rk.rk4(dadiab.dadiab,7,theta,dtheta,y)
        var,dvar = fl.filmatrix(i,y,dy,var,dvar)
    return var,dvar
