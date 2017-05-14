#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zz'

# isothermal model

from engine import *
import volume as vol
vc, ve, vb, dvc, dve, dvb = vol.volume(theta)
vt = vk/tk+vr/tr+vh/th

p0 = 1/((vc+vb)/tk+vt+(vpul+ve)/th)
p0 = p0*pm/np.mean(p0)
p1 = 1/((vc+vb)/tk+vt+(vpul+ve-vgclc*(p0/pm)**(-1/gama))/th)
p1 = p1*pm/np.mean(p1)

while np.max(np.abs(p1-p0))>1:
	p0 = p1
	p1 = 1/((vc+vb)/tk+vt+(vpul+ve-vgclc*(0.5*(p0+p1)/pm)**(-1/gama))/th)
	p1 = p1*pm/np.mean(p1)

p = p1
vge = vpul+ve-vgclc*(p/pm)**(-1/gama)
m = p*((vc+vb)/tk+vt+(vge)/th)/r

"""
deltap = p1-p0
x = np.zeros((nt,7))
x[:,0] = p
x[:,1] = deltap
x[:,2] = m
x[:,3] = vge
x[:,4] = vc
x[:,5] = ve
x[:,6] = vb
data = open('datap.txt','w')
for line in x:
	print(*line,file=data)
data.close()
"""
