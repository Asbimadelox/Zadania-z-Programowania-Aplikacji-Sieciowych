# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 17:31:36 2021

@author: Modecom
"""

import socket


addr = '127.0.0.1'
port = 50000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((addr, port))



while True:
    liczba = input("Podaj daną liczbę: ")
    liczba = str(liczba)
    sock.send(bytes(liczba, "utf-8"))
    odp = sock.recv(1024)
    print(odp.decode("utf-8"))