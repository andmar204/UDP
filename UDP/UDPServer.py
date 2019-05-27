#UDPServer.py

#UDP (SOCK_DGRAM) is a datagram-based protocol. You send one 
#datagram and get one reply and then the connection terminates.
from socket import socket, SOCK_DGRAM, AF_INET
from timeit import default_timer as timer
import time
import random

#Create a UDP socket 
#Notice the use of SOCK_DGRAM for UDP packets
#AF_INET is the Internet address family for IPv4
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
print("Waiting for connections")
while True:
    # Receive the client packet along with the address it is coming from
    # This random integer will allow the server to randomly drop packets.
    # Basically, I get a random number between 0 and 9, and if it's less
    # than or equal to 5, it'll continue as normal, but if it's greater
    # than 5, it'll simply not do anything with the message it received.
    val = random.randint(0,9)
    message, address = serverSocket.recvfrom(2048)

    if val <= 5:
        # Start a timer, capitalize the message from the client, send it back, 
        # and stop the timer.
        start = timer()
        print(str(message, 'utf-8'), address)
        message = message.upper()
        serverSocket.sendto(message, address)
        end = timer()

serverSocket.close()


#Configure the server so that it randomly drops packets.

#Include information about how long each response took. This will be the RTT.
#This is the time it took to print, capitalize, and send the message back. This
# doesn't include the time it took for the message to get from the client to
# here.
print("Time elapsed (server):", (end - start) * 1000, "ms")
