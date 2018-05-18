
buzzer_file='/dev/rtbuzzer0'
sensor_file='/dev/rtlightsensor0'

while True:
 with open(sensor_file,'r') as se:
  print se.read()

