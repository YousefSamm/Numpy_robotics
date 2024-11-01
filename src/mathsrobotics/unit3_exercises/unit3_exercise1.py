import numpy as np 
from utilities import plot_function
x=np.arange(0.0,100.0,1)
f=0.5*x**2+3
plot_function(x,f,'f = (1/2)*x^2 + 3')
df = 1*x
plot_function(x,df,'df = x')
d2f = [1 for i in range(len(x))]
plot_function(x,d2f,'d2f = x')