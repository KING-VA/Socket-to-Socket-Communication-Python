import socket,os
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("", 5005))
k = ' '
size = 1024

while(1):
    print "Enter 1 to send image"
    k = raw_input()
    client_socket.send(k)
    k = int (k)
    if(k == 1):
        print "Enter file name\n"
        strng = raw_input()
        client_socket.send(strng)
        size = client_socket.recv(1024)
        size = int(size)
        print "The file size is - ",size," bytes"
        size = size*2
        strng = client_socket.recv(size)
        print "\nThe contents of that file - "
        print strng
