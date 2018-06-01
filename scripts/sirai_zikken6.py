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

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    area=cv2.countNonZero(mask)
    print area
    
    if (area>1000):
        right_motor(400)
        left_motor(400)
        
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    
    
    
    if k == 27:
        break

cv2.destroyAllWindows()
