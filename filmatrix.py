#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zz'

# fill the var dvar matrices with values of y, dy
def filmatrix(j, y, dy, var, dvar):
	ROWV = 27
	ROWD = 20
	for i in range(ROWV):
		var[i,j] = y[i]
	for i in range(ROWD):
		dvar[i,j] = dy[i]

	return var, dvar
