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
 
 
 
def plt_show(plt, width, dpi=100):
    bytes = io.BytesIO()
    plt.savefig(bytes, format='png', dpi=dpi)
    if hasattr(plt, "close"):
        plt.close()
    bytes.seek(0)
    base64_string = "data:image/png;base64," + \
        base64.b64encode(bytes.getvalue()).decode("utf-8")
    return "<img src='" + base64_string + "' width='" + str(width) + "'>"
 
def main(inputs):
    global s
    global r
    global b
    s = inputs['s']
    r = inputs['r']
    b = inputs['b']
    def attractor(axis_x, axis_y, axis_z, r=inputs['r'], s=inputs['s'], b=inputs['b']):
        x_coordinate = s*(axis_y - axis_x)
        y_coordinate = r*axis_x - axis_y - axis_x*axis_z
        z_coordinate = axis_x*axis_y - b*axis_z
        return x_coordinate, y_coordinate, z_coordinate
    dt = 0.01
    diffcoord = 10000
    xs = np.empty(diffcoord + 1)
    ys = np.empty(diffcoord + 1)
    zs = np.empty(diffcoord + 1)
    xs[0], ys[0], zs[0] = (0., 1., 1.05)
    for i in range(diffcoord):
        x_coordinate, y_coordinate, z_coordinate = attractor(xs[i], ys[i], zs[i])
        xs[i + 1] = xs[i] + (x_coordinate * dt)
        ys[i + 1] = ys[i] + (y_coordinate * dt)
        zs[i + 1] = zs[i] + (z_coordinate * dt)
    global n
    n = 100
    cmap = plt.cm.hsv
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(xs, ys, zs, lw=0.5, color=cmap(i/n))
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    plot1 = plt_show(plt, 400)
    wi = 400
    he = 300
    dpi = 50
    u0, v0, w0 = 0, 1, 1.05
    tmax, n = 100, 10000
    def lor(t, X, si, be, rh):
        u, v, w = X
        up = -s*(u - v)
        vp = r*u - v - u*w
        wp = -b*w + u*v
        return up, vp, wp
    soln = solve_ivp(lor, (0, tmax), (u0, v0, w0), args=(s, b, r),
                    dense_output=True)
    t = np.linspace(0, tmax, n)
    x, y, z = soln.sol(t)
    plt2 = plt.figure(figsize=(wi/dpi, he/dpi))
    ax = plt2.gca(projection='3d')
    plt2.subplots_adjust(left=0, right=1, bottom=0, top=1)
    se = 10
    cmap = plt.cm.hsv
    for i in range(0,n-se,se):
        ax.plot(x[i:i+se+1], y[i:i+se+1], z[i:i+se+1], color=cmap(i/n), alpha=0.4)
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        ax.set_zlabel("Z Axis")
    plot2 = plt_show(plt2, 700)
    plt.close('all')
    jet = cm = plt.get_cmap('jet') 
    values = range(10)
    cNorm  = colors.Normalize(vmin=0, vmax=values[-1])
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)
    def solve_lorenz(N=12, angle=0.0, max_time=8.0, s=inputs['s'], b=inputs['b'], r=inputs['r']):
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1], projection='3d')
        ax.grid(False)
        ax.set_xlim((-25, 25))
        ax.set_ylim((-35, 35))
        ax.set_zlim((5, 55))
        def lorenz_deriv(x_y_z, t0, s=s, b=b, r=r):
            x, y, z = x_y_z
            return [s * (y - x), x * (r - z) - y, x * y - b * z]
        np.random.seed(1)
        x0 = -10 + 20 * np.random.random((N, 3))
        t = np.linspace(0, max_time, int(500*max_time))
        x_t = np.asarray([integrate.odeint(lorenz_deriv, x0i, t)
                        for x0i in x0])
        colors = plt.cm.prism(np.linspace(0, 1, N))
        for i in range(N):
            x, y, z = x_t[i,:,:].T
            lines = ax.plot(x, y, z, '-', c=colors[i])
            plt.setp(lines, linewidth=1)
        ax.view_init(30, angle)
        return t, x_t
    t, x_t = solve_lorenz(angle=0, N=12)
    plt.figure(2)
    lines = plt.plot(t,x_t[1,:,0],t,x_t[1,:,1],t,x_t[1,:,2])
    plt.setp(lines, linewidth=1)
    lines = plt.plot(t,x_t[2,:,0],t,x_t[2,:,1],t,x_t[2,:,2])
    plt.setp(lines, linewidth=1)
    lines = plt.plot(t,x_t[10,:,0],t,x_t[10,:,1],t,x_t[10,:,2])
    plt.setp(lines, linewidth=1)
    plot3 = plt_show(plt, 400)
    pos_init1 = [1.0, 1.0, 1.0]
    pos_init2 = [1.0, 1.0, -1.0]
    t = np.linspace(0, 100, 10000)
    def Te(init, t):
        xb, yb, zb = init
        return s * (yb - xb), (xb*(r-zb))-yb, (xb*yb)-(b*zb)
    positions1 = odeint(Te, pos_init1, t)
    positions2 = odeint(Te, pos_init2, t)
    plt4 = plt.figure(figsize = [12, 12])
    ax = plt4.gca(projection = "3d")
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.grid(True)
    ax.plot(positions1[:, 0], positions1[:, 1], positions1[:, 2], alpha = 1, color = 'darkorange', linewidth = 1)
    ax.plot(positions1[0, 0], positions1[0, 1], positions1[0, 2], marker = '.', color = 'darkorange')
    plt4 = plt.figure(figsize = [12, 12])
    plt.xlabel('Time (seconds)')
    plt.ylabel('x position (m)')
    plt.grid(True)
    plt.plot(t, positions1[:, 0], alpha = 1, color = 'red', linewidth = 1)
    plt.plot(t, positions2[:, 0], alpha = 1, color = 'darkviolet', linewidth = 1)               
    plt.xlim(0, 20)
    plt.legend()
    plot4 = plt_show(plt4, 350)
    Reds = cm = plt.get_cmap('Reds') 
    values = range(10)
    cNorm  = colors.Normalize(vmin=0, vmax=values[-1])
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=Reds)
    def solve_lorenz(N=12, angle=0.0, max_time=8.0, s=inputs['s'], b=inputs['b'], r=inputs['r']):
        global plt5
        plt5 = plt.figure()
        ax = plt5.add_axes([0, 0, 1, 1], projection='3d')
        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')
        ax.axis('on')
        ax.set_xlim((-25, 25))
        ax.set_ylim((-35, 35))
        ax.set_zlim((5, 55))
        def lorenz_deriv(x_y_z, t0, s=s, b=b, r=r):
            x, y, z = x_y_z
            return [s * (y - x), x * (r - z) - y, x * y - b * z]
        np.random.seed(1)
        x0 = -10 + 20 * np.random.random((N, 3))
        t = np.linspace(0, max_time, int(500*max_time))
        x_t = np.asarray([integrate.odeint(lorenz_deriv, x0i, t)
                        for x0i in x0])
        colors = plt.cm.prism(np.linspace(0, 1, N))
        for i in range(N):
            x, y, z = x_t[i,:,:].T
            lines = ax.plot(x, y, z, '-', c=colors[i])
            plt.setp(lines, linewidth=1)
        ax.view_init(30, angle)
        plt.show()
        return t, x_t
    t, x_t = solve_lorenz(angle=0, N=12)
    plt.figure(2)
    lines = plt.plot(t,x_t[1,:,0],t,x_t[1,:,1],t,x_t[1,:,2])
    plt.setp(lines, linewidth=1)
    lines = plt.plot(t,x_t[2,:,0],t,x_t[2,:,1],t,x_t[2,:,2])
    plt.setp(lines, linewidth=1)
    lines = plt.plot(t,x_t[10,:,0],t,x_t[10,:,1],t,x_t[10,:,2])
    plt.setp(lines, linewidth=1)
    global plt5
    plot5 = plt_show(plt5, 350)
    # ---------------------------------------------------------------------
    # THREE ATTRACTOR AXES PERSPECTIVES
 
    t = inputs['t']
    tf = inputs['tf']
    h = inputs['h']
    #These variables were used since they can be easily found for comparison, for example, in Wikipedia under the Lorenz system article
 
    #Derivative function to work with RK4 loop
    def derivative(p,t):
        x = p[0]
        y = p[1]
        z = p[2]
        global s
        global r
        global b
        s = inputs['s']
        r = inputs['r']
        b = inputs['b']
        return np.array([s * (y - x), x * (r - z) - y, (x * y) - (b * z)])
 
    time = np.array([]) #Empty time array to fill for the x-axis
    x = np.array([]) #Empty array for x values
    y = np.array([]) #Empty array for y values
    z = np.array([]) #Empty array for z values
    p = np.array([1.0, 1.0, 1.0]) #Initial conditions array
 
    for i in range(True):
        while (t <= tf ):
            #Appending values to graph
            time = np.append(time, t)
            z = np.append(z, p[2])
            y = np.append(y, p[1])
            x = np.append(x, p[0])
            #RK4 Step method
            k1 = h*derivative(p,t)
            k2 = h*derivative(p+k1/2,t+h/2)
            k3 = h*derivative(p+k2/2,t+h/2)
            k4 = h*derivative(p+k3,t+h)
            p += (k1+2*k2+2*k3+k4)/6
            #Updating time value with step size
            t = t + h
 
    n = 100
    cmap1 = plt.cm.spring
    cmap2 = plt.cm.winter
    cmap3 = plt.cm.summer
 
    plt8, (ax3,ax2,ax1) = plt.subplots(1,3, figsize = (15, 5))
    ax1.plot(x, y, color=cmap1(i/n))
    ax1.set_title("X Axis , Y Axis")
    ax2.plot(x, z, color=cmap2(i/n))
    ax2.set_title("X Axis , Z Axis")
    ax3.plot(y, z, color=cmap3(i/n))
    ax3.set_title("Y Axis , Z Axis")
    plt.show()
 
 
    plot8 = plt_show(plt8, 900)
 
    # ---------------------------------------------------------------------
    
    #-----------------------------------------------------------------------

 
    return {
        "Image_1": plot1,   # primary attractor
        "Image_2": plot2,   # secondary attractor
        "Image_3": plot3,   # chart 1 
        "Image_4": plot4,   # chart 2
        "Image_5": plot5,    # subsec attractor
        "Image_8": plot8,   # three persepectives
    }
 