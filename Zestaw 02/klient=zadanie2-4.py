# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 13:06:30 2021

@author: Modecom
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

imie = input("Podaj imie do analizy")
imie = str(imie)

s.send(bytes(imie, "utf-8"))

while 1:
    msg = s.recv(1024)
    print(msg.decode("utf-8"))