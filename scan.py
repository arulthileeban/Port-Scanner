import socket,sys

IP = raw_input("Enter Host: ")
IP = socket.gethostbyname(IP)
port_choice=input("* 1 - Common Protocol Ports\n* 2 - ICANN Ports\n* 3 - Private Ports\n* 4 - All ports\nEnter choice: ")

port_range={1:[0,1024],2:[1024,49153],3:[49152,65536],4:[0,65536]}
try:
	for port in range(port_range[port_choice][0],port_range[port_choice][1]):
		sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		conn=sock.connect_ex((IP,port))
		if conn == 0 :
			print "Port %s open" % str(port)
		sock.close()
except Exception as e:
	print e
