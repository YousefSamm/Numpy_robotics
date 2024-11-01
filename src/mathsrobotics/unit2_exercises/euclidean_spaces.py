import numpy as np
x = np.array((3,4))
norm = np.sqrt(sum(x_i**2 for x_i in x))
print('Norm by definetion', norm)
norm_numpy=np.linalg.norm(x)
print('Norm calculated with numpy', norm_numpy)