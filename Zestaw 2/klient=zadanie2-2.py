# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 18:42:06 2021

@author: Modecom
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

liczba = input("Podaj wartosc do potęgi")
liczba = str(liczba)

s.send(bytes(liczba, "utf-8"))

while 1:
    msg = s.recv(1024)
    print(msg.decode("utf-8"))