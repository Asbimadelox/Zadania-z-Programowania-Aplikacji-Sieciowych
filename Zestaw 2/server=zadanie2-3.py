# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 13:23:21 2021

@author: Modecom
"""

import socket
import time

ip = "192.168.1.17"
host = "DESKTOP-72E2F8E"
proto = socket.getprotobyname('tcp')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto) #utworzenie gniazda
s.bind((socket.gethostname(), 1234)) #dowiazanie do portu 8888
s.listen(5)

while 1:
    client,addr = s.accept() # odebranie polaczenia   
    msg = client.recv(1024)
    msg = msg.decode("utf-8")
    print(msg)
    
    print( 'Polaczenie z '+str(addr))
    client.send(bytes(time.ctime(time.time()), "utf-8")) # wyslanie danych do klienta

