#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zz'

from engine import *
import adiab
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

# adiabatic pt model
var,dvar = adiab.adiab()

'''
data = open('data.txt','w')
for line in var:
    print(line,file = data)
data.close()
'''
