import matplotlib.pyplot as plt
import numpy as np


def graph(formual, x_range):
    x = np.array(x_range)
    y = eval(formual)

    print(y, type(y))

    plt.plot(x, y)
    plt.show()


def graph_with_out_eval(formula, x_range):
    x = np.array(x_range)
    y = formula(x)
    print(formula)
    #ar1 = [1,2.3,4,5,6,7,8]
    #ar2 = [8,2.3,4,-5,6,7,1]
    plt.plot(x, y)
    #plt.plot(ar1,ar2)
    plt.show()

def graph_with_sub_function(formual,x_range):
    x = np.array(x_range)
    y = formual(x)
    plt.plot(x,y)
    plt.show()

def my_formula(x):
    return x**3+2*x-4

if __name__ == '__main__':
    # graph('x**3+2*x-4',range(-10,11))
    graph_with_out_eval(lambda x: x ** 3 + 2 * x - 4, range(-10,11))
    graph_with_out_eval(lambda x: x ** 3 + 2 * x - 4, np.arange(-10,11))

    graph_with_sub_function(my_formula,np.arange(-10,11))
