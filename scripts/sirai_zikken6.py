import cv2
import numpy as np
import rospy

cap = cv2.VideoCapture(0)

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

while(1):

    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    lower_red = np.array([150,10,15])
    upper_red = np.array([180,255,255])

    

    mask_b = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_r = cv2.inRange(hsv, lower_red, upper_red)

    area_b=cv2.countNonZero(mask_b)

    area_r=cv2.countNonZero(mask_r)

    
    right_motor(0)
    left_motor(0)
    
    if (area_b>area_r and area_b):
        right_motor(400)
        left_motor(400)
        print 'blue'
    elif(area_r>area_b and area_r):
        right_motor(-400)
        left_motor(-400)
        print 'red'

