import numpy as np
from utilities import plot_derivative
    
# define the x values
x = np.arange(0,6,1)

# function f(x)
f = x**2
df = 2*x

# plot the function
plot_derivative(x,f,df,'f = x^2','df = 2*x')
