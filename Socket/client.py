from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)

list1 = [ 0.0, 0.1, 0.2 ]
print (list1)
for i in range(len(list1)):
    list1[i] = str(list1[i])

print (list1)

str1 = ' '.join(list1)
print (str1)

msg = ("Hello you there!").encode('utf-8')  
print (msg)

msg = str1.encode('utf-8')  
print (msg)

s.sendto(msg, ('192.168.15.102', 6667)) 
# server address
