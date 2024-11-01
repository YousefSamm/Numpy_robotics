import numpy as np
from utilities import plot_distro

x = [0,1,2,3,4,5,6,7,8,9,10]
p = [0.,0.04,0.08,0.12,0.16,0.2,0.16,0.12,0.08,0.04,0.]

plot_distro(x,p,'normal')
E = np.dot(x,p)
print('Expected value: ',E)

E_X_2 = E**2
E_X2 = np.dot(np.multiply(x,x),p)
Var = E_X2 - E_X_2
print('Variance of X: ',Var)
STD = np.sqrt(Var)
print('Standard deviation of X: ',STD)