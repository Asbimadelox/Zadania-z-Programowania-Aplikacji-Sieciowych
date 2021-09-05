# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 18:24:13 2021

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

    