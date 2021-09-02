# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 19:58:53 2021

@author: Modecom
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

msg = s.recv(1024)
print(msg.decode("utf-8"))