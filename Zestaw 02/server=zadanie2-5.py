# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 13:51:14 2021

@author: Modecom
"""

import socket
import pickle

ip = "192.168.1.17"
host = "DESKTOP-72E2F8E"
proto = socket.getprotobyname('tcp')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto) #utworzenie gniazda
s.bind((socket.gethostname(), 1234)) #dowiazanie do portu 8888
s.listen(5)

while 1:
    client,addr = s.accept() # odebranie polaczenia   
    msg = client.recv(4096)
    msg = pickle.loads(msg)
    print(msg)
    
    print( 'Polaczenie z '+str(addr))
    client.send(bytes("DAne odebrano pomyslnie! ", "utf-8")) # wyslanie danych do klienta