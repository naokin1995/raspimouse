


led_file='/dev/rtled0'
switch_file='/dev/rtswitch0'


while True:
  with open(switch_file,'r') as s:
    if (s==0):
      with open(led_file,'w') as f:
       print >>f,'1'
  