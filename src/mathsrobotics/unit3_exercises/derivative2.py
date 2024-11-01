import numpy as np
from utilities import plot_derivative
    
# define the x values
x = np.arange(0,6,1)

# function f(x)
f = 3*x
df = [3 for i in range(len(x))]

# plot the function
plot_derivative(x,f,df,'f = 3*x','df = 3')
