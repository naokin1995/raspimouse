
buzzer_file='/dev/rtbuzzer0'
sensor_file='/dev/rtlightsensor0'

while True:
 with open(sensor_file,'r') as se:
  data=se.read()
  list_data=data.split(' ')
  print list_data[0] + ' ' + list_data[3]
   if (int(list_data[0]) <200 and int(list_data[3])<200):
    with open(buzzer_file,'w') as b:
     print >> b,'10000'
   else:
    with open(buzzer_file,'w') as b:
     print >> b,'0'
     
    
  

