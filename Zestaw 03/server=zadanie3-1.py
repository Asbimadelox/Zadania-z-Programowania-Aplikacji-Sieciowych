import random
import socket

zgoda = False
password = "Velvet"
proto = socket.getprotobyname('tcp')


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1769))
s.listen(5)

while True:
    
    
    client, addr = s.accept()
    bufor = client.recv(1024)
    bufor = bufor.decode("utf-8")
    
    if bufor == password:
        zgoda = True
        client.send(bytes(zgoda, ))
        s.close()
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        
        

while True:
    client, addr = s.accept()
    print("Connected: " + addr[0])

    while True:
        data = client.recv(1024)
        if not data:
            break;
        print ('I receive = ' + data.decode('utf-8'))
        client.send(data)
    
    client.close()

s.close()
