# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 13:33:11 2021

@author: Modecom
"""

import socket

 

address = "192.168.1.17"
print(address)
host = socket.gethostbyaddr(address)
host = host[0]
print('Address: ', address, '\n' 'Host: ', host)