
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
   if (msg.axes[1]==1):
     right_motor(400)
     left_motor(400)
   elif (msg.axes[1]==-1):
     right_motor(-400)
     left_motor(-400)
   elif(msg.axes[1] and msg.axes[1] == 0):
     right_motor(0)
     left_motor(0)
  
  

rospy.init_node("joy_subscriber")
sub = rospy.Subscriber('joy',Joy,callback,queue_size=1)
rospy.spin()



