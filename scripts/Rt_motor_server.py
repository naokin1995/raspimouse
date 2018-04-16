#!/usr/bin/env python
import rospy
import time
from Rt_motor import Rt_motor_driver

class Rt_motor_server:
  def __init__(self):
    self.motor_driv=Rt_motor_diver()
    self.motor_driv.r_motor(400)
    self.motor_driv.l_motor(400)
    
    time.sleep(10)
    
    self.motor_driv.r_motor(0)
    self.motor_driv.l_motor(0)
    
    
    
    
if __name__=='__main__':
  ins=Rt_motor_server()
