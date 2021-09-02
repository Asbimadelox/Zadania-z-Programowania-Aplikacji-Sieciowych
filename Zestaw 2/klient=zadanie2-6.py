# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 17:21:52 2021

@author: Modecom
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

message = input("Wpisz wiadomosc do wyslania")
message = str(message)

#s.send(bytes(message, "utf-8"))

i = 0
while 1:
    if i < len(message):
        mess = message[i]
    if i >= len(message):
        break
    s.send(bytes(mess, "utf-8"))
    i += 1
    
    
print("Gotowe!")