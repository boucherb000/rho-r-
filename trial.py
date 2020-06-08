#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np



def my_function(x):
    return 4*x**3 + 3*x**2 - 2*x + 1


x_vals = np.linspace(0,10,num=5)

f_vals = my_function(x_vals)

fig = plt.figure()

ax = fig.add_subplot()

ax.plot(x_vals,f_vals, color='xkcd:mauve')

fig.savefig("trial_plot.png")

integral = np.trapz(f_vals,x_vals)
print(integral)

derv = np.gradient(f_vals,x_vals)
print(derv)
