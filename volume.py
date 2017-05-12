import numpy as np
def volume(t):
    vc = vclc + 0.5*vswc*(1-np.cos(2*pi*f*t))
    ve = vcle + 0.5*vswe*(1-np.cos(2*pi*f*t+theta))
    dvc = 0.5*vswc*np.sin(2*pi*f*t)*2*pi*f
    dve = 0.5*vswe*np.sin(2*pi*f*t+theta)*2*pi*f
    return vc, ve, dvc, dve
