import numpy as np 
def vectorleng(vec):
    length= np.linalg.norm(vec)
    return length
def sum_of_vectors(v1,v2):
    return v1 + v2
def calc_hypotenusa(leng1, leng2):
    hypotenusa=np.sqrt(leng1**2 + leng2**2)
    return hypotenusa

# define vectors
leg_1 = np.array((4,0))
leg_2 = np.array((0,3))

# calculate sum of these vectors
hypotenusa = sum_of_vectors(leg_1,leg_2)
print('Vector hypotenusa is: ',hypotenusa)

# calculate lengths of vectors
leg_1_len = vectorleng(leg_1)
leg_2_len = vectorleng(leg_2)
hypotenusa_len = vectorleng(hypotenusa)
print('Length of vectors: leg_1: ',leg_1_len, ', leg_2: ',leg_2_len,', hypotenusa: ',hypotenusa_len)

# apply Pythagorean Theorem
pyth_len = calc_hypotenusa(leg_1_len,leg_2_len)
print('Pythagorean Theorem gives a hypotenusa length of: ',pyth_len)
