#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty
import numpy as np
#import skfuzzy as sk
from csv import reader



x = 0
y = 0
theta = 0
x2 = 0
y2 = 0
theta2= 0

def poseCallback1(pose_message):
    global x
    global y
    global theta

    x = pose_message.x
    y = pose_message.y
    theta = pose_message.theta

def poseCallback2(pose_message):
    global x2
    global y2
    global theta2

    x2 = pose_message.x
    y2 = pose_message.y
    theta2 = pose_message.theta
    
##################################################################################


def go_to_goal (xgoal, ygoal):


    #leer csv

    with open('/home/inigo/catkin_ws/src/fis/src/velocidad.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_l = list(csv_reader)

        vel_lin = [list(map(float, sublist)) for sublist in list_l]

    with open('/home/inigo/catkin_ws/src/fis/src/omega.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_a = list(csv_reader)

        vel_ang = [list(map(float, sublist)) for sublist in list_a]


    while(True):
        if theta > math.pi:
            pm_theta = (theta-(2*math.pi))*(180/math.pi)
        else:
            pm_theta = theta*(180/math.pi)

        print("theta: ", round(theta,3), "\t pm_theta: ", round(pm_theta,3))
        gtheta = (math.atan2(ygoal-y, xgoal-x))*(180/math.pi)
        print("gtheta: ", round(gtheta,3))
        dtheta = gtheta - pm_theta

        
        if dtheta>180:
            dtheta = int(dtheta - 360)
        if dtheta<-180:
            dtheta = int(dtheta + 360)
        else:
            dtheta = dtheta
        print("dtheta: ", int(dtheta))


        dist = math.sqrt((x2 - x)**2 + (y2 - y)**2)


        print(dist)
        print(dtheta)

        cmd_vel = Twist()
        cmd_vel.linear.x = 0.0
        cmd_vel.linear.y = 0.0
        cmd_vel.linear.z = 0.0
        cmd_vel.angular.x = 0.0
        cmd_vel.angular.y = 0.0
        cmd_vel.angular.z = 0.0

        cmd_vel.linear.x = vel_lin[int(dist)][0]*2
        cmd_vel.angular.z = -vel_ang[int(dtheta)][0]

        velocity_publisher.publish(cmd_vel)

        break

##################################################################################
#suscripciones
if __name__ == '__main__':
    try:
        

        rospy.init_node('turtlesim_motion_pose', anonymous = True)

        cmd_vel_topic = '/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size = 10)

        position_topic1 = "/turtle1/pose"
        pose_subscriber1 = rospy.Subscriber(position_topic1, Pose, poseCallback1)

        position_topic2 = "/turtle2/pose"
        pose_subscriber2 = rospy.Subscriber(position_topic2, Pose, poseCallback2)

        #Entrada

        time.sleep(1.0)
        
        while(True):     
            
            go_to_goal(x2,y2)
                   
    except rospy.ROSInterruptException:        
        pass
