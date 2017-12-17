import socket,sys

IP = raw_input("Enter Host: ")
IP = socket.gethostbyname(IP)


for port in range(1,1025):
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	conn=sock.connect_ex((IP,port))
	if conn == 0 :
		print "Port %s open" % str(port)
	sock.close()
		
