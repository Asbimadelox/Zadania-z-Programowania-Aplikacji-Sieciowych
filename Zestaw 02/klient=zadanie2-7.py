# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 18:14:48 2021

@author: Modecom
"""

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 1234))

while True:
    nazwa_pliku = input("Wpisz nazwe pliku, który chcesz pobrać: ")
    
    if nazwa_pliku != "":
        sock.send(bytes(nazwa_pliku, "utf-8"))
        port2 = sock.recv(1024)
        port2 = int(port2.decode("utf-8"))
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock2.connect((socket.gethostname(), port2))
        
        while True:
            plik = sock2.recv(1024).decode("utf-8")
            file = open(nazwa_pliku,"w")
            file.write(plik)
            print("Sciagnieto!")
            file.close()
            sock2.close()
            break
    else:
        continue


