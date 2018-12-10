import socket
import sys

def stop():
    if KeyboardInterrupt:
        sys.exit(0)

print("Selection automatique (1) ou manuelle (2) : ")
i = int(input())

if (i == 1):
    UDP_IP = "10.160.108.4"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print ("Received message : ", data.decode(), "from", addr)
        print ("Send message : ")
        MESSAGE = str(input())
        sock.sendto(MESSAGE.encode(), (addr))
        print ("Message sent at : ", addr)
        stop()
        
elif (i == 2):
    UDP_IP = "10.160.108.4"
    UDP_PORT = 5005
    print("Enter IP address destination : ")
    UDP_IP2 = str(input())

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        print ("Send message : ")
        MESSAGE = str(input())
        sock.sendto(MESSAGE.encode(), (UDP_IP2, UDP_PORT))
        print ("Message sent at : ", UDP_IP2, UDP_PORT)
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print ("Received message : ", data.decode(), "from", addr)
        stop()
