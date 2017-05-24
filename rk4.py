#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zz'

' Classical fourth order Runge-Kutta method '

def rk4(f,n,x,dx,y):
	x0 = x
	y0 = y
	y,dy1 = f(x0,y)
	for i in range(n):
		y[i] = y0[i]+0.5*dx*dy1[i]
	xm = x0+0.5*dx
	y,dy2 = f(xm,y)
	for i in range(n):
		y[i] = y0[i]+0.5*dx*dy2[i]
	y,dy3 = f(xm,y)
	for i in range(n):
		y[i] = y0[i]+dx*dy3[i]
	x = x0+dx
	y,dy = f(x,y)
	for i in range(n):
		dy[i] = (dy1[i]+2*(dy2[i]+dy3[i])+dy[i])/6
        y[i] = y0[i]+dx*dy[i]
	return x,y,dy
