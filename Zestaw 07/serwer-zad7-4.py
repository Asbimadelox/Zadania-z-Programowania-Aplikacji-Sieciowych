# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 19:23:45 2021

@author: Modecom
"""

import socket
from _thread import start_new_thread
import random



def obsluga(klient,adres):

    while True:
        odp_pr = random.randint(0, 101)
        print("Sprawdzanie odpowiedzi")
        while True:
            odp = klient.recv(1024)
            odp = odp.decode("utf-8")
            odp = int(odp)
            
            if odp_pr > odp:
                klient.send("Liczba za mala. Spróbuj ponownie.".encode("utf-8"))
            elif odp_pr < odp:
                klient.send("Liczba za duża. Spróbuj ponownie.".encode("utf-8"))
            else:
                klient.send("Zgadłes! Gratulacje!".encode("utf-8"))
                break
        klient.close()
        return
            
        
        
host = '127.0.0.1'
port = 50000

sock = socket.socket()#socket.AF_INET, socket.SOCK_STREAM
sock.bind((host, port))
sock.listen(5)

print("Uzyskano polaczenie.")
while True:
    client, addr = sock.accept()
    start_new_thread(obsluga,(client,addr))



sock.close()