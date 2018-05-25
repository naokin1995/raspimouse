
import rospy
from sensor_msgs.msg import Joy

motor_file='/dev/rtmotoren0'
motor_filel='/dev/rtmotor_raw_l0'
motor_filer='/dev/rtmotor_raw_r0'
with open (motor_file,'w') as m:
 print >> m,'1'

def right_motor(num):
 with open (motor_filer,'w') as mr:
       print >> mr,str(num)
def left_motor(num):
 with open (motor_filel,'w') as ml:
       print >> ml,str(num)
 
def callback(msg):
  print msg.axes[1]*100.0+msg.axes[0]*100
  
  right_motor(int(msg.axes[1]*100.0+msg.axes[0]*100)*10)
  left_motor(int(msg.axes[1]*100.0+msg.axes[0]*-100)*10)
  
  

rospy.init_node("joy_subscriber")
sub = rospy.Subscriber('joy',Joy,callback,queue_size=1)
rospy.spin()



