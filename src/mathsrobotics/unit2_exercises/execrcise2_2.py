import numpy as np
from utilities import plot_vectors_3D

# define the rotation function
def rotate(vec,angle):
    angle = angle*np.pi/180 # convert degrees to radians
    R = np.array(((np.cos(angle),-np.sin(angle),0),
                  (np.sin(angle),np.cos(angle),0),
                  (0,0,1)))
    rotated = np.dot(R,vec)
    return rotated

# define initial vector
vec = np.array((4,0,0))
# angle to turn
angle = 90

# call the function
vec_r = rotate(vec,angle)

# plot vectors
plot_vectors_3D((vec,vec_r))
    
