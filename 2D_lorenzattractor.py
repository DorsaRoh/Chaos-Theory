import numpy as np
import matplotlib.pyplot as plt

# import user input parameters
from parameters import sigma, rho, beta

def main(inputs):
    s = inputs['s']
    r = inputs['r']
    b = inputs['b']
    
    def attractor(axis_x, axis_y, axis_z):
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

    fig = plt.figure(figsize=(15, 5))  # Adjusting the size for horizontal alignment

    # X vs Y plot
    ax1 = fig.add_subplot(1, 3, 1)  # Changed to 1 row and 3 columns
    ax1.plot(xs, ys, lw=0.5, color='springgreen')
    ax1.set_xlabel("X Axis")
    ax1.set_ylabel("Y Axis")
    ax1.set_title("X vs Y")

    # Y vs Z plot
    ax2 = fig.add_subplot(1, 3, 2)  # Changed to 1 row and 3 columns
    ax2.plot(ys, zs, lw=0.5, color='coral')
    ax2.set_xlabel("Y Axis")
    ax2.set_ylabel("Z Axis")
    ax2.set_title("Y vs Z")

    # X vs Z plot
    ax3 = fig.add_subplot(1, 3, 3)  # Changed to 1 row and 3 columns
    ax3.plot(xs, zs, lw=0.5, color='magenta')
    ax3.set_xlabel("X Axis")
    ax3.set_ylabel("Z Axis")
    ax3.set_title("X vs Z")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    inputs = {'s': sigma, 'r': rho, 'b': beta}
    main(inputs)
