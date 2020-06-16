#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

def rho(r):
    return 1/(r * (1 + r)**2)

r_vals = np.linspace(0,10,num=5)

y = rho(r_vals)

print(y)

fig = plt.figure()

ax = fig.add_subplot()

ax.plot(r_vals, y, color='xkcd:mauve')

fig.savefig("rho_plot.png")
