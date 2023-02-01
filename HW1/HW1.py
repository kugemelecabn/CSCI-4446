from matplotlib import pyplot as plt
import numpy as np
import sys, pdb

def logistic_map(x0, R):
    return (R * x0 * (1 - x0)),

def plot_a():
    x0 = float(sys.argv[1])
    R = float(sys.argv[2])
    x_arr = []
    x_arr.append(x0)
    n_arr = np.arange(0, 101, 1)
    for x in range(0, 100):
        if x > 0:
            x_arr[x] = x_arr[x][0]
        x_arr.append(logistic_map(x_arr[x], R))
    x_arr[-1] = x_arr[-1][0]
    plt.title('x0 = ' + str(x0) + '  R = ' + str(R))
    plt.xlabel('n')
    plt.ylabel('x_n')
    plt.scatter(n_arr, x_arr)
    plt.show()
    for x in range(0, 100):
        plt.scatter(x_arr[x], x_arr[x+1])
    plt.title('x0 = ' + str(x0) + '  R = ' + str(R))
    plt.xlabel('x_n')
    plt.ylabel('x_n + 1')
    plt.show()
    for x in range(0, 98):
        plt.scatter(x_arr[x], x_arr[x+2])
    plt.title('x0 = ' + str(x0) + '  R = ' + str(R))
    plt.xlabel('x_n')
    plt.ylabel('x_n + 2')
    plt.show()
    

if __name__ == '__main__':
    plot_a()