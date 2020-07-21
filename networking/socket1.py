import socket

mysock  = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)


fout = open('mbox.txt','w')
while True:
	data = mysock.recv(1)
	if(len(data)<1):
		break
	# print(data.decode())
	fout.write(data.decode())

fout.close()
mysock.close()
exit()