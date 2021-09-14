# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 13:11:03 2021

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
        
        
    print("Uruchamianie serwera")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((addr, port))
    sock.listen(5)
    
    pol, adres = sock.accept()
    print("Łączenie...")
    file = open("zdjecia.txt", "r")
    while True:
        
        
        print("oczekiwanie na rozkaz")
        rozkaz = pol.recv(1024).decode("utf-8")#rozkaz
        print("otrzymano rozkaz")

        if rozkaz == "GET_IMAGE":
            nazwa = file.readline()
            if nazwa == "":
                pol.send(bytes("NOPE", "utf-8"))
                break
            
            nazwa = str(nazwa)
            nazwa = nazwa.strip("\n")
            print(nazwa)
            jpg = open(nazwa, "rb") #!
            print(nazwa)
            send_jpg = jpg.read()
            jpg_size = len(send_jpg)
            
            pol.sendall(bytes(str(jpg_size), "utf-8"))#wielkosc
            print("Wysłanie wielkosci pliku")
            
            pol.sendall(bytes(send_jpg))#sam plik
            print("Wysłanie samego pliku")

            pol.sendall(bytes(nazwa, "utf-8"))#nazwa pliku
            print("Wysłąnie nazwy pliku")
            
            print("Zdjęcie wysłane")
            print("   ")
            jpg.close()
        else:
            print("ERROR \r\n")
            sys.exit(1)
    
    
            
