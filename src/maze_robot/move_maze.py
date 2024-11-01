import rospy
from turtlebot_project import *
import numpy as np

if __name__=='__main__':
    node_name='move_out_of_the_maze'
    rospy.init_node(node_name, anonymous=True)
    rospy.loginfo('Initializing node {}'.format(node_name))

    mover=TurtlebotProject()
    mover.move()