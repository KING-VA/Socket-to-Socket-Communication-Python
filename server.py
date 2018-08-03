import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "your_IP"
port = 5060
print (host)
print (port)
serversocket.bind((host, port))

user_name = "VA" # can be anything - also might want to consider using openssl for security - this is just the basics
pass_word = "VA" # can be anything - also might want to consider using openssl for security - this is just the basics

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        count = 0
        
        while True:
            if (count == 0):
                while True:
                    self.sock.send("Please enter username\n".encode())
                    d1 = self.sock.recv(4096).decode()
                    ret1 = client.username(d1)
                    if ret1 == True:
                        self.sock.send("Please enter password\n".encode())
                        d2 = self.sock.recv(4096).decode()
                        ret2 = client.password(d2)
                        if ret2 == True:
                            self.sock.send("Access granted\n".encode())
                            count = count + 1
                            break
                        else:
                            s.close()
                    else:
                        s.close()
            else:
                v = self.sock.recv(4096).decode()
                print('Client sent:', v)
                result = client.checker(v)
                if (result == True):
                    self.sock.send("Welcome V.".encode())
                    self.sock.close()
                    break
                else:
                    self.sock.send("User Unauthorized. Ending Connection".encode())
                    self.sock.close()
                    #do nothing - allow reconnection
                    break
    def checker(data):
        if (data == "V"):
            return True
        else:
            return False
    def username(data):
        if (data == user_name):
            return True
        else:
            return False
    def password(data):
        if (data == pass_word):
            return True
        else:
            return False
            

serversocket.listen(5)
print ('server started and listening')
while True:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)

