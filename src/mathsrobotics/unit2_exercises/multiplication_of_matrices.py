import numpy as np
import matplotlib.pyplot as plt
A = np.array(((1,2,3), (4,5,6)))
B = np.array(((1,1,1)))
print('Matrix A: ')
print (A)
print('Matrix B: ')
print (B)
sum_=A+B
print('Sum of matrices A + B: ')
print(sum_)
multiply_=A*3
print('Multiplication of matrix A * 3: ')
print(multiply_)
product_=np.dot(A,B)
print('Product pf matrices A * B + C: ')
print('C =', product_)