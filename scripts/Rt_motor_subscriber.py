#!/usr/bin/env python
import rospy
import time
from Rt_motor import Rt_motor_driver
from sensor_msgs.msg import Joy


class Rt_Motor_Subscriber:
  def __init__(self):
    
    self.speed=600.0
    
    self.motor_driv=Rt_motor_driver()
    rospy.init_node('Rt_motor_Subscriber')
    self.sub=rospy.Subscriber('/joy',Joy,self.callback)
    rospy.spin()
    

    
  def callback(self,message):
    print message.axes
    print message.axes[1]*self.speed
    print message.axes[1]*self.speed
    print message.axes[0]*self.speed
    print message.axes[0]*self.speed
    
    if message.axes[0] > 0:
      self.motor_driv.r_motor(int(message.axes[1]*self.speed + message.axes[0]*self.speed))
      self.motor_driv.l_motor(int(message.axes[1]*self.speed - message.axes[0]*self.speed))
      
    elif message.axes[0] < 0:
      self.motor_driv.r_motor(int(message.axes[1]*self.speed + message.axes[0]*self.speed))
      self.motor_driv.l_motor(int(message.axes[1]*self.speed - message.axes[0]*self.speed))
      
    else:
      self.motor_driv.r_motor(int(message.axes[1]*self.speed))
      self.motor_driv.l_motor(int(message.axes[1]*self.speed))
    
    

  def test_drive(self):
    self.motor_driv.r_motor(400)
    self.motor_driv.l_motor(400)
    
    time.sleep(10)
    
    self.motor_driv.r_motor(0)
    self.motor_driv.l_motor(0)


if __name__=='__main__':
  ins=Rt_Motor_Subscriber()
