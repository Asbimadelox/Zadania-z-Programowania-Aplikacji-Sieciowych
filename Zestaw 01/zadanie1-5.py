# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:40:40 2021

@author: Modecom
"""

import socket

ip= input("Wpisz IP: ") #'192.168.1.17'
#port_list = [20, 30, 80, 8080, 31, 32, 33, 475]

for port in range(0,65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    wynik = s.connect_ex((ip, port))
    
    if wynik == 0:
        print('Port: '+str(port)+" otwarty")
        
    s.close()
    '''    
    else:
        print('Port: '+str(port)+" zamknięty")
    '''
        
        
host = input("Wpisz hostname tutaj: ") #socket.gethostname()

for port in range(0,65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    wynik = s.connect_ex((host, port))
    
    if wynik == 0:
        print('Port: '+str(port)+" otwarty")
        
    s.close()
    '''
    else:
        print('Port: '+str(port)+" zamknięty")
    '''