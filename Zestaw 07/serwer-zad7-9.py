# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 17:32:08 2021

@author: Modecom
"""

import socket
import select

def obsluga(dane):
    while True:
        #msg = klient.recv(1024)
        #msg = msg.decode("utf-8")
        dane = int(dane)
        print("Obliczanie z ciagu Fibonaciego")
        if dane == 1:
            wynik = 0
        elif dane == 2:
            wynik = 1
        else:
            a = 0
            b = 1
            c = 0
            dane -= 1
            for x in range(dane):
                c = a + b
                a = b
                b = c
            wynik = a
        wynik = str(wynik)
        print("Obliczone!")
        return wynik
             
    
    
host = '127.0.0.1'
port = 50000

sock = socket.socket()#socket.AF_INET, socket.SOCK_STREAM
sock.bind((host, port))
sock.listen(5)

ins = [sock]
ous = []
data = {}
adrs = {}


print("Uzyskano polaczenie.")
try:
    while True:
        i, o, e = select.select(ins, ous, [])
        for x in i:
            if x is sock:
                client, addr = sock.accept()
                ins.append(client)
                adrs[client] = addr
            else:
                dane = x.recv(1024).decode("utf-8")
                print(dane)
                wynik = obsluga(dane)
                print(wynik)
                data[x] = wynik
                if x not in ous: ous.append(x)
        for x in o:
            tosend = data.get(x)
            if tosend:
                print(tosend)
                x.send(bytes(tosend, "utf-8"))
                tosend = ""
                del data[x]
               
finally:
    sock.close()

    