
motor_file='/dev/rtmotoren0'
motor_filel='/dev/rtmotor_raw_l0'
motor_filer='/dev/rtmotor_raw_r0'
sensor_file='/dev/rtlightsensor0'

with open (motor_file,'w') as m:
 print >> m,'1'
with open (motor_filel,'w') as ml:
 print >> ml,'100'
with open (motor_filelr,'w') as mr:
 print >> mr,'100'
 
while True:
 with open(sensor_file,'r') as se:
  data=se.read()
  list_data=data.split(' ')
  print list_data[0] + ' ' + list_data[3]
 if (int(list_data[0])>200 and int(list_data[3])>200):
  with open (motor_filel,'w') as ml:
   print >> ml,'0'
  with open (motor_filelr,'w') as mr:
   print >> mr,'0'



