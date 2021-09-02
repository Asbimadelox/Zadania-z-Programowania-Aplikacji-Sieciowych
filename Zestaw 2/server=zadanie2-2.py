# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 18:41:46 2021

@author: Modecom
"""

import socket


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
    msg = int(msg)
    print("Potęgowanie liczby")
    msg = msg*msg
    msg = str(msg)
    print( 'Polaczenie z '+str(addr))
    client.send(bytes(msg, "utf-8")) # wyslanie danych do klienta