import numpy as np
from utilities import plot_distro

# set range limits
a = 2
b = 6
# set x values
x = np.arange(a,b,0.01)
# set value p = 1/b-a for all values
y = [((b-a)**(-1)) for i in range(len(x)-2)]

plot_distro(x,y,'uniform')

plot_distro(x,y,'cumulative')

mu = 4
# scale
sigma = 0.5
# set prob N(mu,sigma) for all values
rv = norm(mu,sigma)
y = rv.pdf(x)

plot_distro(x,y,'normal')
y = 0.125*(x-a)

plot_distro(x,y,'cumulative')