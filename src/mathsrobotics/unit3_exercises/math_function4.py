import numpy as np 
from utilities import plot_function_3d
x_1=np.arange(0,6,1)
x_2=np.arange(0,6,1)
x_1, x_2=np.meshgrid(x_1, x_2)
f = -3*x_1 + x_2**3

plot_function_3d(x_1,x_2,f,'f = -3*x_1 + x_2^3')