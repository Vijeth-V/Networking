#My Name: Vijeth Venkatesha, My Partner: Tejasri lakkamasani
import socket
import random
import time

server_ip = "192.168.1.217"
server_port = 3310
blazerId = input("Enter the BlazerId - ")

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(ip_address)

print("Student Started")

print("")

# Create a TCP socket to make connection
print("Creating TCP socket")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))
print("Connected to the robot")

# Send the blazerId
client_socket.send(blazerId.encode())
print("Sent BlazerId to robot server - "+ blazerId +"\n")

# Receive the response from the robot server 
response = client_socket.recv(1024)
socket_s1 = response.decode()
print("TCP port received from robot server ")
client_socket.close()

print("started student server with port no - " + socket_s1)
listenSocket_S1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listenSocket_S1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listenSocket_S1.bind((ip_address, int(socket_s1)))
listenSocket_S1.listen(5)


studentS1, address = listenSocket_S1.accept()
student_S1_IP = address[0]
# listenSocket_S1.close()

new_ports = studentS1.recv(1024).decode()
print(" \nReceived 2 ports from robot server")
port1=new_ports.split(',')[0]
port2=new_ports.split(',')[1]
print('Port 1 -',port1)
print('Port 2 -',port2 + "\n")

num = random.randint(6, 9)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.connect((server_ip, int(port1)))
udp_socket.send(str(num).encode())

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((ip_address, int(port2)))

while True:
    transmitMessage, new_port1_addr = s.recvfrom(1024)
    print("message received from robot server: " + transmitMessage.decode())
    if transmitMessage:
        break

print("\nSending the recieved message to robot 5 times: ")
for i in range(0, 5):
    udp_socket.send(transmitMessage)
    time.sleep(1)
    print("Packet %d" %(i+1)+ " sent")
exit()