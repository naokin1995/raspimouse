
buzzer_file='/dev/rtbuzzer0'
sesor_file='/dev/rtsemsor0'

while True:
 with open(sensor_file,'r') as se:
  print se.read()

