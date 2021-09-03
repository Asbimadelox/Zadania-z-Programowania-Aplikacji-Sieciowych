# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 17:04:59 2021

@author: Modecom
"""

import socket
import sys

if __name__ == '__main__':
        
    try:
        port = 115
        assert port > 0
    except:
        sys.stderr.write("error: invalid port\n")
        sys.exit(1)
        
    proto = socket.getprotobyname('tcp')
    print("Serwer się uruchamia")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto)
    sock.bind(("127.0.0.1", port))
    sock.listen(5)
    
    while True:
        
        pol, adres = sock.accept()
        
        nazwa_pliku = pol.recv(1024)
        nazwa_pliku = nazwa_pliku.decode("utf-8")
        
        try:
            file = open(nazwa_pliku, "w")
            pol.send(bytes("Nazwa pliku przyjęta!", "utf-8"))
        except:
            sys.stderr.write("error: wrong url or the lack of file! \n")
            sys.exit(1)
        
            
        try:    
            dane = pol.recv(1024).decode("utf-8")
            file.write(dane)
            pol.send("Dane zapisane!".encode("utf-8"))
        except:
            sys.stderr.write("error: Writing file has failed! \n")
            sys.exit(1)
        
        file.close()
        pol.close()
                
        
        
        