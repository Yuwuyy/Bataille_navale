import socket
UDP_IP = "10.160.108.4"
UDP_PORT = 5005
MESSAGE= (b"Hello, Thomas!")


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sesndto(MESSAGE, (UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("received message : ", data.decode(), "from",addr)
    #sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print ("send message :")
    MESSAGE2= str(input())
    sock.sendto(MESSAGE2.encode(), (addr))
