#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zz'

import numpy as np
from engine import *
def volume(theta):
    vc = vclc + 0.5*vswc*(1-np.cos(theta+phi))
    ve = vcle + 0.5*vswe*(1-np.cos(theta))
    vb = vclb + 0.5*vswb*(1+np.cos(theta))
    dvc = 0.5*vswc*np.sin(theta+phi)
    dve = 0.5*vswe*np.sin(theta)
    dvb = -0.5*vswb*np.sin(theta)

    return vc, ve, vb, dvc, dve, dvb
