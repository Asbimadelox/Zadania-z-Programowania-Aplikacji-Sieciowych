# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 15:30:35 2021

@author: Modecom
"""

import socket
import sys

if __name__ == '__main__':
        
    try:
        addr = '127.0.0.1'
        port = 115
        assert port > 0
    except:
        sys.stderr.write("error: invalid port\n")
        sys.exit(1)
    
    while True:
       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       sock.connect((addr, port))
    
       nazwa_pliku = input("Wpisz sciezke do pliku: \n")
       
       
       if nazwa_pliku != "":
           try:
               plik = open(nazwa_pliku, "r")
               dane = plik.read()
               sock.send(nazwa_pliku.encode("utf-8"))
               wiad = sock.recv(1024).decode("utf-8")
               print(wiad)
           except:
               sys.stderr.write("error: failed sending\n")
               sys.exit(1)
       else:
           sys.exit(0)
   
               
   
       try:
           sock.send(dane.encode("utf-8"))
           wiad = sock.recv(1024).decode("utf-8")
           print(wiad)
       except:
           sys.stderr.write("error: failed sending\n")
           sys.exit(1)            
       
       plik.close()
       sock.close()
    
    
    
        
        