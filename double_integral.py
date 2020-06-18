#!/usr/bin/env python3
from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate as interp

def rho(r):
    return 1/(r * (1 + r)**2)

r_vals = np.linspace(1e-10,10,num=5)

rho_vals = rho(r_vals)

def Phi(r):
    f = lambda y, x: y**2 * rho(y)/x**2
    return -integrate.dblquad(f, r, 100, lambda x: 0, lambda x: x)[0]

print(Phi(1))


phi_vals = [Phi(rr) for rr in r_vals]
print(phi_vals)

derv = np.gradient(rho_vals,phi_vals)
print(derv)

sec_derv = np.gradient(derv,phi_vals)
print(sec_derv)

sec_derv_func = interp.interp1d(phi_vals, sec_derv, fill_value='extrapolate')

def f(E):
    f = lambda phi: sec_derv_func(phi) * 1/np.sqrt(phi-E)
    return integrate.quad(f, E, 0)[0]
print(f(-0.5))
