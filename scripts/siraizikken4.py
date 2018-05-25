
import rospy
from sensor_msgs.msg import Joy


def callback(msg):
  print msg.axes[0]
  print msg.axes[1]


rospy.init_node("joy_subscriber")
sub = rospy.Subscriber('joy',Joy,callback,queue_size=1)
rospy.spin()



