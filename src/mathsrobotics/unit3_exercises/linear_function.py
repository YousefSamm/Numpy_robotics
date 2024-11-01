import numpy as np
from utilities import plot_equation

# define the x values
T_C = np.arange(0,6,1)

# function T_F(T_C)
T_F = 1.8*T_C + 32

# plot the equation
plot_equation(T_C,T_F,'T_F = 1.8*T_C + 32','Temperature in Celsius','Temperature in Fahrenheits')
