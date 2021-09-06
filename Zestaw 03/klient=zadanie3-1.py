import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((socket.gethostname(), 1769))

while True:
    bufor = input("Wpisz haslo do serwera: ")
    
    if bufor != "":
        sock.send(bytes(bufor, "utf-8"))
        bufor2 = sock.recv(1024).decode("utf-8")
        if str(bufor2) == "Haslo prawidlowe!":
            port2 = sock.recv(1024).decode("utf-8")
            port2 = int(port2)
            sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock2.connect((socket.gethostname(), port2))
            
            while True:
                wiad = sock2.recv(1024).decode("utf-8")
                print(wiad)
                sock2.close()
                break
            
        else:
            print(str(bufor2))
            print(" ")        
    else:
        continue
    

