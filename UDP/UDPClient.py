#UDPClient.py

from socket import socket, SOCK_DGRAM, AF_INET
import threading
import sys

#This function will close the client socket and let
# you know that it's been closed.
def closeSocket():
    clientSocket.close()
    print("Time exceeded 1 sec. Client socket closed.")
    sys.exit(0)

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ')
clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))

#This will start a timer that will count for one second. If it reaches
# one second, it'll call closeSocket.
timer = threading.Timer(1.0, closeSocket)    
timer.start()

try:
    modifiedMessage, addr = clientSocket.recvfrom(2048)

    #If the program gets here before the timer has finished counting its
    # one second, then the timer will be canceled since it received the
    # message and we don't have to close the socket any more.
    timer.cancel()
    print(str(modifiedMessage, '-utf-8'), addr)
    clientSocket.close()
except:
    #This program works, but it always raises an exception, because of the
    # sys.exit(0) on line 12. Therefore, I just put that print statement so
    # it could "do" something.
    print("")

#Allow the client to give up if no response has been received within 1 second.
