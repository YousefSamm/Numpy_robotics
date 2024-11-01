import numpy as np
from utilities import plot_equation
t=np.arange(-1,1,0.1)
x_0=2
w=3
phi=0.5
x_t=x_0*np.sin(w*t+phi)
plot_equation(t,x_t,'x(t)= x_0*sin(w*t+phi)','Time t','Position x(t)')