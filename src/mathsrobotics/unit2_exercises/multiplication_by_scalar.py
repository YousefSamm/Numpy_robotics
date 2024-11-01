import numpy as np
import matplotlib.pyplot as plt
from utilities import plot_vectors
vector = np.array((1,2))
alpha = 2
multiplication_=alpha*vector
plot_vectors([vector,multiplication_], 'sum')