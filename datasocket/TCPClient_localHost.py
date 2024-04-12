###########################################
# TCP client code Example:   
# Send a message and get a capitalized reply from server     
###########################################
from socket import *
serverName = '172.30.1.45'#define server host
serverPort = 12000 #port number 는 4자리이상(>1024) 사용 권고
clientSocket = socket(AF_INET, SOCK_STREAM) #TCP client socket open
clientSocket.connect((serverName,serverPort)) #TCP connection with server
sentence = input("Input lowercase sentence:")
clientSocket.send(sentence.encode()) #send a message to server
modifiedSentence = clientSocket.recv(1024) #replyed message from server
print("From Server:", modifiedSentence.decode())
clientSocket.close() #close socket 
