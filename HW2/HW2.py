from matplotlib import pyplot as plt
import numpy as np
import sys, pdb

def logistic_map(x0, R):
    return (R * x0 * (1 - x0))

def plot_a():
    x0 = float(sys.argv[1])
    l = int(sys.argv[2]) # blocks transients
    m = int(sys.argv[3]) # total number of iterates
    r_arr = np.arange(2.8, 4, .01)
    num_r_points = len(r_arr)
    x_arr = []
    x_arr.append(x0)
    n_arr = np.arange(0, 101, 1)
    for r in r_arr:
        for x in range(0, m):
            x_arr.append(logistic_map(x_arr[x], r))
        x_arr.pop(-1)
        for z in range(0, l):
            x_arr.pop(z)
        r_plot = np.ones(len(x_arr)) * r
        plt.scatter(r_plot, x_arr, .01)
    plt.title('Bifurcation Diagram')
    plt.xlabel('R')
    plt.ylabel('x_n')
    plt.show()

    

if __name__ == '__main__':
    plot_a()