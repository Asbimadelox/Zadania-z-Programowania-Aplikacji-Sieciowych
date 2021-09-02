
"""
Created on Tue Aug 10 17:40:37 2021

@author: Modecom
"""
import socket


ip = "192.168.1.17"
host = "DESKTOP-72E2F8E"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #utworzenie gniazda
s.bind((socket.gethostname(), 1234)) #dowiazanie do portu 8888
s.listen(5)

while 1:
	client,addr = s.accept() # odebranie polaczenia
	print( 'Polaczenie z '+str(addr))
	client.send(bytes("YESSSSSSSSSSSSSSSSSSSSSSS!", "utf-8")) # wyslanie danych do klienta



