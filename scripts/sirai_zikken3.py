
motor_file='/dev/rtmotoren0'
motor_filel='/dev/rtmotor_raw_l0'
motor_filer='/dev/rtmotor_raw_r0'

with open (motor_file,'w') as m:
 print >> m,'1'
with open (motor_filel,'w') as ml:
 print >> ml,'400'
with open (motor_filer,'w') as mr:
 print >> mr,'400'


