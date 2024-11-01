import numpy as np 

def decide_left_or_right(limit=0.8):
    number=np.random.uniform()
    print('the generated number is: ', number)
    if number<limit:
        return True
    else:
        return False
decide_left_or_right()