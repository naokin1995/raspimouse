
import rospy
from sensor_msgs.msg import Joy


def callback(msg):
  print msg


rospy.init_node("joy_subscriber")
sub = rospy.Subscriber('joy',Joy,callback,queue_size=1)



