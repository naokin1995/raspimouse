import rospy
import time


class Rt_motor_driver:
  
  
  def __init__(self):
    self.init_file='/dev/rtmotoren0'
    self.__init_motor()
    
    
    
  def __init_motor(self):
    try:
      with open(init_file,'w') as f:
        print >> f,'1'
        
    except:
      rospy.logerr("Cannot write to"+ self.init_file)
      
      
      
if __name__ =="__main__":
  ins=Rt_motor_driver()
      
      
