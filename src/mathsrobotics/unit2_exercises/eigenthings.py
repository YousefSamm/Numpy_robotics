import numpy as np 
A=np.array(((1,0,0), (0,2,0), (0,0,3)))
print('Matrix A: ')
print(A)
A_eigvalues, A_eigvectors= np.linalg.eig(A)
print('Matrix A eigenvalues: ',A_eigvalues)
print('Matrix A eigenvect: ')
print(A_eigvectors)