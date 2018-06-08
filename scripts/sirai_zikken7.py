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
                    print (strTemp)
                else:
                    pass
                data = ""
        else:
            data += str(sock.recv(1024).decode('utf-8'))





