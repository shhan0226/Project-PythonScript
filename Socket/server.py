from socket import socket, AF_INET, SOCK_DGRAM

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('192.168.15.102', 6667))
# server addresses

while True:
    msg, addr = sock.recvfrom(1024)
    print("Got message from %s: %s" % (addr, msg))
    temp = msg.decode('utf-8')
    print(temp)

