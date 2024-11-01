import numpy as np
import matplotlib.pyplot as plt
from utilities import plot_vectors
v = np.array(((1,0)))
R=np.array(((0, -1), (1,0)))
w=np.dot(R, v)
print('Product of matrices 2 = R * v =', w)
plot_vectors((v,w), 'rotation')