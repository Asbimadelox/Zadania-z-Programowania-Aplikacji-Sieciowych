# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 12:17:28 2021

@author: Modecom
"""
import socket

#hostname = socket.gethostname()

local_ip = input("Wpisz dany adres IP")


print(local_ip)

try:
    socket.inet_aton(local_ip)
    print("Ten adres IP jest prawidłowy.")
except socket.error:
    print("Ten adres IP NIE jest prawidłowy.")