import random
import socket

password = "Velvet"
proto = socket.getprotobyname('tcp')


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM, proto)
s.bind((socket.gethostname(), 1769))
s.listen(5)

while True:
    client, addr = s.accept()
    
    while True:
        #client.send(bytes("Prosze podac haslo: ", "utf-8"))
        bufor = client.recv(1024)
        bufor = bufor.decode("utf-8")
        bufor = str(bufor)
    
        if bufor == password:
            zgoda = True
            client.send(bytes("Haslo prawidlowe!","utf-8" ))
            xyz = random.randint(1000,65535)
            xyz = str(xyz)
            client.send(bytes(xyz, "utf-8"))
            sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto)
            xyz = int(xyz)
            sock2.bind((socket.gethostname(), xyz))
            print("Serwer się przygotowuje do wysłania wiadomosci...")
            sock2.listen(5)
        
            while True:
                client2, addr2 = sock2.accept()
                wiad = "Ostatnie sztuki w żabce przy Instytucie Informatyki"
                client2.send(wiad.encode("utf-8"))
                client2.close()
                break
        else:
            client.send(bytes("Błędne hasło!", "utf-8"))

        
        