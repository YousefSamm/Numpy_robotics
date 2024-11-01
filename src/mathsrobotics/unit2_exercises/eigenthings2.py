import numpy as np

# create a matrix with numpy
B = np.array(((-6,3), 
              (4,5)))
print('Matrix B: ')
print(B)

# eigenvalues and eigenvectors of a matrix with numpy
B_eigvalues, B_eigvectors = np.linalg.eig(B)
print('Matrix B eigenvalues: ',B_eigvalues)
print('Matrix B eigenvect: ')
print(B_eigvectors)
print('Eigenvalue ',B_eigvalues[1])
print('A x : ',np.dot(B,B_eigvectors[:,1]))
print('lambda x : ',B_eigvalues[1]*B_eigvectors[:,1])

#first eigenvalue(-7)
#gives the following result: 'A x : ', array([ 6.64078309, -2.21359436])) 
# create a matrix with numpy
#B = np.array(((-6,3), 
#              (4,5)))
#print('Matrix B: ')
#print(B)

# eigenvalues and eigenvectors of a matrix with numpy
#B_eigvalues, B_eigvectors = np.linalg.eig(B)
#print('Matrix B eigenvalues: ',B_eigvalues)
#print('Matrix B eigenvect: ')
#print(B_eigvectors)
#print('Eigenvalue ',B_eigvalues[0])
#print('A x : ',np.dot(B,B_eigvectors[:,0]))
#print('lambda x : ',B_eigvalues[0]*B_eigvectors[:,0])