# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 13:12:16 2021

@author: Modecom
"""

import socket
import sys

if __name__ == '__main__':
    
    try:
        addr = socket.gethostname()
        port = 1234
        assert port > 0
    except:
        sys.stderr.write("error: invalid port\n")
        sys.exit(1)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((addr, port))

    while True:
        nazwa_pliku = input("Nacinij enter, by móc pobrać plik graficzny")
    
        if nazwa_pliku == "":
            sock.send(bytes("GET_IMAGE", "utf-8"))#rozkaz
        
            wielkosc = sock.recv(1024).decode("utf-8")# wielkosc pliku
            
            if str(wielkosc) == "NOPE":
                break
            
            print(wielkosc)
            wielkosc = int(wielkosc) 
            

            plik = sock.recv(wielkosc)# sam plik
            
            nazwa = sock.recv(1024).decode("utf-8")#nazwa pliku
            nazwa = str(nazwa)
            print(nazwa)
            file = open(nazwa,"wb")
            file.write(plik)
            print("Sciagnieto "+str(nazwa)+" !")
            print("  ")
            file.close()
        else:
            continue
        
        
        
    sock.close()