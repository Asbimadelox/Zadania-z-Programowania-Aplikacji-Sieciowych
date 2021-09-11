# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:29:49 2021

@author: Modecom
"""

import socket
import ssl

addr = '127.0.0.1'
port = 50000
server_cert = 'server.crt'
client_cert = 'client.crt'
client_key = 'client.key'

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=server_cert)
context.load_cert_chain(certfile=client_cert, keyfile=client_key)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = context.wrap_socket(sock, server_side=False, server_hostname=addr)
conn.connect((socket.gethostname(), port))



while True:
    liczba = input("Podaj daną liczbę: ")
    liczba = str(liczba)
    conn.send(bytes(liczba, "utf-8"))
    

    odp = conn.recv(1024)
    print(odp.decode("utf-8"))