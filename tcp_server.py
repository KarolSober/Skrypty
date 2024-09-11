#! /usr/bin/python3

import socket

TCP_IP = "192.168.181.190"
TCP_PORT = 6996
BUFFER_SIZE = 100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen

conn, addr = s.accept()
print ('Adres polaczenia: '. addr )

while 1:

	data=conn.recv(BUFFER_SIZE)
	if not data:break
	print ("Otrzymano dane: ", data)
	conn.send(data) #echo

conn.close



s = socket.socket()
s.connect(("10.0.2.15", 22))
answer = s.recv(1024)
print (answer)
s.close
