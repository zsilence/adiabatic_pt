#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zz'

' Classical fourth order Runge-Kutta method '

def rk4(df,n,x,dx,y):
	x0 = x
	y0 = y
	y,dy1 = df(x0,y)
	for i in range(1,n+1):
		y(i) = y0(i)+0.5*dx*dy1(i)
	xm = x0+0.5*dx
	y,dy2 = df(xm,y)
	for i in range(1,n+1):
		y(i) = y0(i)+0.5*dx*dy2(i)
	y,dy3 = df(xm,y)
	for i in range(1:n+1):
		y(i) = y0(i)+dx*dy3(i)
	x = x0+dx
	y,dy = df(x,y)
	for i in range(1,n+1):
		dy(i) = (dy1(i)+2*(dy2(i)+dy3(i))+dy(i))/6
		y(i) = y0(i)+dx*dy(i)
	return x,y,dy
