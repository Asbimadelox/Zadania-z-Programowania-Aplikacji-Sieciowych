# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 15:32:07 2021

@author: Modecom
"""

import socket
import requests

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 1234))



#while True:
wiad =  '''GET / HTTP/1.1\r\n
\r\n'''
sock.send(bytes(wiad, "utf-8"))
print("Wysłano")
wiad2 = sock.recv(1024).decode("utf-8")
print("Odebrano")
print(wiad2)
