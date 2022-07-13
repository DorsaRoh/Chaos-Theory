
import time
startTime = time.time()
import numpy as np
import matplotlib.pyplot as plt
import base64
import io
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
from scipy.integrate import odeint
from matplotlib import animation
from matplotlib.colors import cnames
from matplotlib import cm
from scipy import integrate
import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib as mpl
 
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
    plot7 = plt_show(plt7, 700)

    return {
        "Image_7": plot7
    }
