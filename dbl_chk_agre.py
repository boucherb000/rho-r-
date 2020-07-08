#!/usr/bin/env python3
from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate as interp

# defining what our rho(r) is

def rho(r):
    return 1/(r * (1 + r)**2)

r_vals = np.logspace(1e-10,1,num=50)

rho_vals = rho(r_vals)

plt.plot(r_vals,rho_vals)
plt.show()


#defining what our phi(r) is and comparing it to the equation 17 and 18

def Phi(r):
    f = lambda y, x: y**2 * rho(y)/x**2
    return -integrate.dblquad(f, r, 100, lambda x: 0, lambda x: x)[0]

print(Phi(1))


phi_vals = [Phi(rr) for rr in r_vals]
print(phi_vals)

#plotting phi

fig = plt.figure()
ax = fig.subplots()
ax.set_title('gravitational potential (phi)')
ax.set_xlabel('r_vals')
ax.set_ylabel('phi_vals')
plt.plot(r_vals, phi_vals, color = 'xkcd:midnight purple')
our_line, = ax.plot(r_vals, phi_vals, marker='$\Phi$', markersize=10)
our_line.set_linestyle((0,(1,3)))
our_line.set_color('xkcd:seafoam')
ax.spines['top'].set_color('black')
ax.set_facecolor('xkcd:white')
plt.show(fig)
fig.savefig("grav_poten_phi.png")

# defining what our psi(r) is as the same in eq. 17 & 18 on the notes

def Psi(r):
    return -(np.log(1 + r)) / r

psi_vals = Psi(r_vals)

print(psi_vals)


# plotting psi


fig = plt.figure()
ax = fig.subplots()
ax.set_title('gravitational potential (psi)')
ax.set_xlabel('r_vals')
ax.set_ylabel('psi_vals')
plt.plot(r_vals, psi_vals, color = 'xkcd:midnight purple')
our_line, = ax.plot(r_vals, psi_vals, marker='$\Psi$', markersize=10)
our_line.set_linestyle((0,(1,3)))
our_line.set_color('xkcd:seafoam')
ax.spines['top'].set_color('black')
ax.set_facecolor('xkcd:white')
plt.show(fig)
fig.savefig("grav_poten_psi.png")

# solving for the derivative of rho(r)

derv = np.gradient(rho_vals,phi_vals)
print(derv)

fig = plt.figure()

ax = fig.add_subplot()

ax.plot(phi_vals, derv, color='xkcd:mauve')
# ax.set_yscale("log")
# ax.set_xscale("log")
plt.show()

# solving for the second derivative of rho(r)

sec_derv = np.gradient(derv,phi_vals)
print(sec_derv)


plt.plot(phi_vals, sec_derv)

plt.show()

# making the second derivative a function

sec_derv_func = interp.interp1d(phi_vals, abs(sec_derv), fill_value='extrapolate')

plt.plot(phi_vals, sec_derv_func(phi_vals))

plt.show()


def f(E):
    f = lambda phi: abs(sec_derv_func(phi)) * 1/abs(np.sqrt(phi-E))
    return integrate.quad(f, E, 0)[0]

E_vals = np.linspace(min(phi_vals)* 0.96,0,num=25)
enrg = [f(E) for E in E_vals]

plt.plot(E_vals, enrg)
plt.show()
print(f(-0.8))
