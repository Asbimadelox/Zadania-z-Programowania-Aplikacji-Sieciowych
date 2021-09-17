# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 12:40:17 2021

@author: Modecom
"""


import socket
#hostname = socket.gethostname()
hostname = input("Wpisz hostname...")
ip_address = socket.gethostbyname(hostname)
print("Hostname: " + hostname)
print("IP Address: " + ip_address)