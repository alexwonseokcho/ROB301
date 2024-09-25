#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import String




def define_move(x,y,z, twist, rate, cmd_pub):




  


   if(x != 0):
       theta_1 = math.tan(y/x)
       twist.angular.z = 0.2 #rad/s
       time_run_z = theta_1 / twist.angular.z
       for i in range(int(time_run_z * 10)):
           cmd_pub.publish(twist)
           rate.sleep()
       twist.angular.z = 0
   else:
       theta_1 = 0
  
   r_1 = math.sqrt(x**2 + y**2)
   twist.linear.x = 0.25
   time_run_x = r_1 / twist.linear.x
   for i in range(int(time_run_x * 10)):
       cmd_pub.publish(twist)
       rate.sleep()
   twist.linear.x = 0


   theta_2 = math.radians(z) - theta_1
   twist.angular.z = 0.7 #rad/s
   time_run_z = theta_2 / twist.angular.z
   print(time_run_z)
   for i in range(int(time_run_z * 10)):
       cmd_pub.publish(twist)
       rate.sleep()
   twist.angular.z = 0
   rate.sleep()
   cmd_pub.publish(twist)


   return


def define_move_curve(x, y, z, twist, rate, cmd_pub):
   r= 1.25
   theta = math.radians(-45)
   time_1 = 8
   distance_1 =  2*math.pi*(r) * (abs(theta) / (2* math.pi))
   twist.linear.x = distance_1/time_1
   twist.angular.z = theta/time_1


   print(str(twist.linear.x) + str(twist.angular.z))


   for i in range (int(time_1*10)):
       cmd_pub.publish(twist)
       rate.sleep()


    r = 0.7
   theta = math.radians(180)
   time_1 = 15
   distance_1 =  2*math.pi*(r)*(theta / (2* math.pi))
   twist.linear.x = distance_1/time_1
   # twist.linear.x = 0
   twist.angular.z = theta/time_1


   print(str(twist.linear.x) + str(twist.angular.z))
   for i in range (int(time_1*10)):
       cmd_pub.publish(twist)
       rate.sleep()
   twist.linear.x = 0
   twist.linear.z = 0
   cmd_pub.publish(twist)








def main():
   rospy.init_node("lab02")
  
   rate = rospy.Rate(10)


   """TODO: publish commands to make robot move to desired pose"""


   """TODO: complete motor publishing functionality here"""
   twist = Twist()
  
   cmd_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
  
   #direct line path
   # define_move(2, 0.5, 135, twist, rate, cmd_pub)


   #waypoints
   # define_move(1, 0, 90, twist, rate, cmd_pub)
   # define_move(0, 1, 90, twist, rate, cmd_pub)
   # define_move(-1, 0, 90, twist, rate, cmd_pub)


   #curve
   define_move_curve(69, 69, 69, twist, rate, cmd_pub)




   # define_move_curve(2, 0.5, 135, twist, rate, cmd_pub)
   # twist.linear.x=0
   # twist.angular.z=0
   cmd_pub.publish(twist)
   rate.sleep()
      




if __name__ == "__main__":
   main()
  
  
  





