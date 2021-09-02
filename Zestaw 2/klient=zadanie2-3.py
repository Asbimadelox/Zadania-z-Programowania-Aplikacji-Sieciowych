# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 13:22:59 2021

@author: Modecom
"""

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

message = input("Wpisz wiadomosc do wyslania")
message = str(message)

s.send(bytes(message, "utf-8"))


while 1:
    msg = s.recv(1024)
    print("Aktualny czas: "+ msg.decode("utf-8"))