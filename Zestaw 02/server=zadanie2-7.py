# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 18:14:25 2021

@author: Modecom
"""

import socket
import random
import os.path
#import requests
import sys

proto = socket.getprotobyname('tcp')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto)
sock.bind((socket.gethostname(), 1234))
print("Serwer się uruchamia")
sock.listen(5)


while True:
    client,addr = sock.accept()
    
    while True:
        msg = client.recv(1024)
        msg = msg.decode("utf-8")
        print("Sprawdzanie, czy plik istnieje...")
        
        if os.path.exists(msg):
            xyz = random.randint(1000,65535)
            xyz = str(xyz)
            client.send(bytes(xyz, "utf-8"))
            sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto)
            xyz = int(xyz)
            sock2.bind((socket.gethostname(), xyz))
            print("Serwer się przygotowuje do wysyłania pliku...")
            sock2.listen(5)
            
            while True: 
                client2, addr2 = sock2.accept()
                file = open(msg, "r")
                data = file.read()
                client2.send(data.encode("utf-8"))
                client2.close()
                break
            
            client.close()
            sys.exit(0)
        else:
            continue