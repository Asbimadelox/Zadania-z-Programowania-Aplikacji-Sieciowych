# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 18:24:42 2021

@author: Modecom
"""
'''
Oprocz stosowania watkow server mozna rowniez przyspieszyć za pomoca 
biblioteki cachetools, a cile mówiąc dekoratora cache (pamieci podrecznej),
 który usprawnia działanie danej funkcji
'''
import socket
from _thread import start_new_thread
from cachetools import cached, TTLCache
import time

@cached(cache= TTLCache(maxsize= 33, ttl = 600))
def obsluga(klient,adres):
    s = time.time()
    while True:
        msg = klient.recv(1024)
        msg = msg.decode("utf-8")
        msg = int(msg)
        print("Obliczanie z ciagu Fibonaciego")
        if msg == 1:
            wynik = 0
        elif msg == 2:
            wynik = 1
        else:
            a = 0
            b = 1
            c = 0
            msg -= 1
            for x in range(msg):
                c = a + b
                a = b
                b = c
            wynik = a
        wynik = str(wynik)
        print("Czas: "+str(time.time() - s))
        klient.send(wynik.encode("utf-8"))
        print("Obliczone!")
    klient.close()
            
        
        
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