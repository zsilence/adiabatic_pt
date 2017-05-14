#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zz'

# fill the var dvar matrices with values of y, dy
def filmatrix(j, y, dy, var, dvar):
	ROWV = 26
	ROWD = 17
	for i in range(1,ROWV,1):
		var[i,j] = y[i]
	for i in range(1,ROWD):
		dvar[i,j] = dy[i]

	return var, dvar
