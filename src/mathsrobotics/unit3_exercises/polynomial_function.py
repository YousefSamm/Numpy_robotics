import numpy as np 
from utilities import plot_equation
radius=np.arange(0,6,1)
Volume=(3/4)*np.pi*radius**2
plot_equation(radius,Volume,'V = (4/3)*pi*r^3','Radius of the sphere','Volume of the sphere')