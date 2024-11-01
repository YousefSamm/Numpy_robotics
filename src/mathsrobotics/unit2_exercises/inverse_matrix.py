import numpy as np
import matplotlib.pyplot as plt
A=np.array(((1,2), (3,4)))
print ('MAtrix A: ')
print(A)
A_inverted=np.linalg.inv(A)
print(A_inverted)