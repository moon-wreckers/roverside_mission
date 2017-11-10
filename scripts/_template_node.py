#!/usr/bin/env python

"""
mynode.py
description of mynode...
"""

__version__     = "0.0.1"
__author__      = "David Qiu"
__email__       = "dq@cs.cmu.edu"
__website__     = "http://mrsdprojects.ri.cmu.edu/2017teami/"
__copyright__   = "Copyright (C) 2017, the Moon Wreckers. All rights reserved."

import rospy
from std_msgs.msg import String, Float32, UInt16
from sensor_msgs.msg import Imu, JointState
from geometry_msgs.msg import Vector3Stamped
from nav_msgs.msg import Odometry, Twist


def mynode():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'mynode' node so that multiple nodes can run
    # simultaneously.
    rospy.init_node('mynode', anonymous=True)

    # you code here...

    rospy.spin()


if __name__ == '__main__':
    try:
        mynode()
    except rospy.ROSInterruptException:
        pass
