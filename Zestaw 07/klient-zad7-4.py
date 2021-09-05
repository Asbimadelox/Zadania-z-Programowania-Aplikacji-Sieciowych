# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 19:24:06 2021

@author: Modecom
"""

import socket


addr = '127.0.0.1'
port = 50000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((addr, port))

#odp = sock.recv(1024)
#print(odp)
x = 1
while True:
    print("-----------------------------------------------------------------")
    print("Odgadywanie wylosowanej liczby.\n")
    print("Próba nr: "+str(x))
    liczba = input("Podaj daną liczbę: ")
    liczba = str(liczba)
    sock.send(bytes(liczba, "utf-8"))
    

    odp = sock.recv(1024)
    odp = odp.decode("utf-8")
    print(odp)
    x += 1
    if odp == "Zgadłes! Gratulacje!":
        sock.close()
        break