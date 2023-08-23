import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

from parameters import inv, endv

def main(inputs):
    global inv
    global endv
    inv = inputs['inv']
    endv = inputs['endv']
    interval = (inv, endv)  # start, end
    accuracy = 0.0001
    reps = 600  # number of repetitions
    numtoplot = 200
    lims = np.zeros(reps)
    plt7, biax = plt.subplots()
    plt7.set_size_inches(16, 9)
    lims[0] = np.random.rand()
    for r in np.arange(interval[0], interval[1], accuracy):
        for i in range(reps-1):
            lims[i+1] = r*lims[i]*(1-lims[i])
        biax.plot([r]*numtoplot, lims[reps-numtoplot:], 'b.', markersize=.02)
    biax.set(xlabel='r', ylabel='X Axis', title='Logistic Map')
    plt.show()

# Calling main function with example inputs
inputs = {'inv': inv, 'endv': env}
main(inputs)
