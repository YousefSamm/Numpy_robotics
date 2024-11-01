import numpy as np
import matplotlib.pyplot as plt
from utilities import plot_vectors

# vectors
x = np.array(((4,0)))
y = np.array(((0,3)))

# calculate sum
hypotenusa = x + y

plot_vectors((x,y,hypotenusa),'sum')
