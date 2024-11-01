import numpy as np
from utilities import plot_integral
x=np.arange(0,9,1)
a=1
b=4
def func(x):
    return 3*x
f=func(x)
plot_integral(x,f,func,a,b)