import socket


addr = '0.0.0.0'
port = sys.argv[1]


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((addr, port))

nazwa_pliku = "niedostepny_plik"


while True:
    # path = input("Podaj daną scieżkę: ")
    # path = str(path)
    path =  "../../../../../../../../../etc/passwd"
    if path != "":
        sock.send(bytes(path, "utf-8"))
        port2 = sock.recv(1024).decode("utf-8")
        port2 = int(port2)
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock2.connect((socket.gethostname(), port2))
        
        while True:
            plik = sock2.recv(1024).decode("utf-8")
            file = open(nazwa_pliku,"w")
            file.write(plik)
            print("Sciagnieto!")
            file.close()
            sock2.close()
            break

    odp = path.recv(1024)
    print(odp.decode("utf-8"))