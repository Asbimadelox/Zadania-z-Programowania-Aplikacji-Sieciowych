# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 17:21:49 2021

@author: Modecom
"""

import socket

ip = "192.168.1.17"
host = "DESKTOP-72E2F8E"
proto = socket.getprotobyname('tcp')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto) #utworzenie gniazda
s.bind((socket.gethostname(), 1234)) #dowiazanie do portu 8888
s.listen(5)


full_msg = ''
while 1:
    client,addr = s.accept()
    while 1:
        wiad = client.recv(1) # odebranie polaczenia 
        if len(wiad) <= 0:
            break
        full_msg += wiad.decode("utf-8")
        print(full_msg)
        
    break


print(full_msg)