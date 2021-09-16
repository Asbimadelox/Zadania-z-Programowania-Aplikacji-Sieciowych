# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 19:04:24 2021

@author: Modecom
"""

import socket
import sys
import requests
#----------------------------------------------------------------------
def proxy_server(webserver, port, conn, data, addr):#serwer docelowy
    try:
        proto = socket.getprotobyname('tcp')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto)
        s.connect((webserver, port))
        s.send(data)
        print("Połączono z serwerem własciwym.")
        
        while True:
            reply = s.recv(2048)
            reply = str(reply)
            if len(reply) > 0:
                conn.send(bytes(reply, "utf-8"))
            else:
                break
        
        
        s.close()
        conn.close()
        
    except socket.error:
        s.close()
        conn.close()
        sys.exit(1)
#-----------------------------------------------------------------
try:
    addr = socket.gethostname()
    port = 1234
    assert port > 0
except:
    sys.stderr.write("error: invalid port\n")
    sys.exit(1)
    
    
print("Uruchamianie serwera") #klient
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((addr, port))
print("Łączenie...")
sock.listen(5)
pol, adres = sock.accept()
while True:    
    data = pol.recv(2048)
    proxy_server("www.httpbin.org", 80, pol, data, adres)

#-----------------------------------------------------------------




    