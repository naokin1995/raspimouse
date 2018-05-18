


led_file='/dev/rtled0'
switch_file='/dev/rtswitch0'


while true:
  with open(switch_file,'r') as s:
    if (s==o):
      with open(led_file,'w') as f:
       print >>f,'1'
  
