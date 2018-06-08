#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import socket
import string
import os
import random
import numpy as np
from numpy.random import *
import time

host = "127.0.0.1"
port = 10500
#p = subprocess.Popen(["./julius_start.sh"], stdout=subprocess.PIPE, shell=True)
#pid = str(p.stdout.read().decode('utf-8')) # juliusのプロセスIDを取得
#time.sleep(5)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

data =""
killword =""

motor_file='/dev/rtmotoren0'
motor_filel='/dev/rtmotor_raw_l0'
motor_filer='/dev/rtmotor_raw_r0'
with open (motor_file,'w') as m:
  m.write('1')

def right_motor(num):
 with open (motor_filer,'w') as mr:
  mr.write(str(num))
def left_motor(num):
 with open (motor_filel,'w') as ml:
  ml.write(str(num))
        
while True:

    while (1):
        if '</RECOGOUT>\n.' in data:
            #data = data + sock.recv(1024)
            strTemp = ""
            for line in data.split('\n'):
                index = line.find('WORD="')
                if index != -1:
                    line = line[index+6:line.find('"',index+6)]
                    strTemp += str(line)
                    word = strTemp.split()
                    print (word[0])
                    if(strTemp=='前進'):
                        right_motor(400)
                        left_motor(400)
                    elif(strTemp=='後進'):
                        right_motor(-400)
                        left_motor(-400)
                    elif(strTemp=='停止'):
                        right_motor(0)
                        left_motor(0)
                    
                    
                else:
                    pass
                data = ""
        else:
            data += str(sock.recv(1024).decode('utf-8'))





