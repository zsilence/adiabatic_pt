#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zz'

' Classical fourth order Runge-Kutta method '

import numpy
def rk4(f,n,x0,dx,y):
    y0 = y
    x = numpy.array( [ x0 ] * n )
    y = numpy.ones(n)
    y[0] = y0
    h = dx
    for i in xrange( n-1 ):
        x[i] = x[i] + i*h
        k1 = h * f( x[i], y[i] )
        k2 = h * f( x[i] + 0.5 * h, y[i] + 0.5 * k1 )
        k3 = h * f( x[i] + 0.5 * h, y[i] + 0.5 * k2 )
        k4 = h * f( x[i]+h , y[i]+ k3 )
        y[i+1] = y[i] + ( k1 + 2.0 * ( k2 + k3 ) + k4 ) / 6.0
    return y
