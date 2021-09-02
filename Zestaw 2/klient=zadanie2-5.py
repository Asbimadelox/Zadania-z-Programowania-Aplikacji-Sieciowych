# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 13:51:34 2021

@author: Modecom
"""

import socket
import pickle

zestaw = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

print("Wpisz poszczególne dane")

liczba_nor = int(input("Wpisz liczbę całkowitą: "))
zestaw.append(liczba_nor)

napis = str(input("Wpisz napis: "))
zestaw.append(napis)

liczba_zmien = float(input("Wpisz liczbę zmiennoprzecinkową: "))
zestaw.append(liczba_zmien)

msg = pickle.dumps(zestaw)


s.send(msg)


while 1:
    msg = s.recv(1024)
    print(msg.decode("utf-8"))
