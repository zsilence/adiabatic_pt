#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zz'

' Classical fourth order Runge-Kutta method '

def rk4(deriv,n,x,dx,y):
	x0 = x
	y0 = y

