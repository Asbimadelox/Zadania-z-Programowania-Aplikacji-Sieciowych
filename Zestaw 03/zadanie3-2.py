# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 17:12:52 2021

@author: Modecom
"""

filepath = "datagram_UDP.txt"
f = open(filepath, "r")

dane = f.readlines()
linia1 = dane[0]
linia2 = dane[2]
linia3 = dane[4]

f.close()
linia1 = linia1.strip('\n')
linia2 = linia2.strip('\n')
linia3 = linia3.strip('\n')

port_nadawczy = linia1[0:2] + linia1[3:5]
port_nadawczy = int(port_nadawczy, 16)


print("Nr źródłowego portu: ")
print(port_nadawczy)
print(" ")

port_odbiorczy = linia1[6:8] + linia1[9:11]
port_odbiorczy = int(port_odbiorczy, 16)

print("Nr docelowego portu: ")
print(port_odbiorczy)
print(" ")

dane_UDP = linia1[24:]
dane_UDP = dane_UDP + " " + linia2
dane_UDP = dane_UDP + " " + linia3

print(dane_UDP)

dane_konwersja = [''.join(chr(int(i, 16)) for i in dane_UDP.split())]

print(" ")
print(dane_konwersja)


print("")
print("Dany pakiet zawiera dane, które zajmują łącznie 28 bajtów.")
