import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(('localhost', 1769))
    while True:
        data = "Hello World"
        s.send(data.encode('utf-8'))
        data = s.recv(1024)
        if not data:
            break
        print ('Response:' + data.decode('utf-8'))
    s.close()
except socket.error:
    print ('Error')
