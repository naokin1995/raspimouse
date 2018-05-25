
import rospy
from sensor_msgs.msg import Joy

rospy.init_node("joy_subscriber")
sub = rospy.Subscriber('joy',Joy,callback,queue_size=1)

def callback(msg):
  print msg

