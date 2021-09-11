# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:30:10 2021

@author: Modecom
"""

import socket
from _thread import start_new_thread
import ssl

import time

server_cert = 'server.crt'
server_key = 'server.key'
client_certs = 'client.crt'

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.verify_mode = ssl.CERT_REQUIRED
context.load_cert_chain(certfile=server_cert, keyfile=server_key)
context.load_verify_locations(cafile=client_certs)

def obsluga(klient):
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
            
        
        
host = '192.168.1.17'
port = 50000

sock = socket.socket()#socket.AF_INET, socket.SOCK_STREAM
sock.bind((host, port))
sock.listen(5)

print("Uzyskano polaczenie.")
while True:
    client, addr = sock.accept()
    conn = context.wrap_socket(client, server_side = True)
    start_new_thread(obsluga,(conn))

    
conn.close()