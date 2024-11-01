import numpy as np
from utilities import plot_vectors

# define function sum
def sum_of_vectors(v1,v2):
    return v1 + v2

# define vectors
leg_1 = np.array((4,0))
leg_2 = np.array((0,3))

# call function sum
sum_ = sum_of_vectors(leg_1,leg_2)

# plot resulting vectors
plot_vectors((leg_1,leg_2,sum_),'sum')

# define function angle
def angle_between_vectors(v1,v2):
    v_prod = np.dot(v1,v2)
    v1_norm = np.linalg.norm(v1)
    v2_norm = np.linalg.norm(v2)
    angle = np.arccos(v_prod/(v1_norm*v2_norm))
    
    angle = angle*180/np.pi
    return angle

# call function angle
alpha_12 = angle_between_vectors(leg_1,leg_2)
alpha_2sum = angle_between_vectors(leg_2,sum_)

# print results
print('The angle between leg_1 and leg_2 is: {:.2f} radians'.format(alpha_12))
print('The angle between leg_2 and the sum of leg_1+leg_2 is: {:.2f} radians'.format(alpha_2sum))
