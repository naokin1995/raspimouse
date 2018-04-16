#!/usr/bin/env python
import rospy
import time


class Rt_motor_driver:
  
  
  def __init__(self):
    self.init_file='/dev/rtmotoren0'
    
    self.__init_motor()
    
    
    
  def __init_motor(self):
    try:
      with open(self.init_file,'w') as f:
        print >> f,'1'
        
    except:
      #rospy.logerr("Cannot write to"+ self.init_file)
      pass

  def __fin_motor(self):
    try:
      with open(self.init_file,'w') as f:
        print >> f,'0'
        
    except:
      #rospy.logerr("Cannot write to"+ self.init_file)
      pass

  def right_motor_driver(self,freq):
    try:
      with open('/dev/rtmotor_raw_r0','w') as f:
        print >> f,str(freq)
        
    except:
      #rospy.logerr("Cannot write to"+ self.init_file)
      pass
    

  def left_motor_driver(self,freq):
    try:
      with open('/dev/rtmotor_raw_l0','w') as f:
        print >> f,str(freq)
        
    except:
      #rospy.logerr("Cannot write to"+ self.init_file)
      pass
      
      
if __name__ =="__main__":
  ins=Rt_motor_driver()
  
  ins.right_motor_driver(400)
  time.sleep(10)
  ins.right_motor_driver(0)
  ins.left_motor_driver(500)
  time.sleep(10)
  ins.left_motor_driver(0)
  
      
      
