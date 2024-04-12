###########################################
# TCP server code Example:   
# Capitalization of the data that client sent   
###########################################
from socket import *
serverPort = 12000 #port number 는 4자리이상(>1024) 사용 권고
serverSocket = socket(AF_INET,SOCK_STREAM) #UDP server socket open
serverSocket.bind(('1.224.174.77',serverPort)) #bind server host IP & port
serverSocket.listen(1) # max no of connection = 1
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept() #TCP connection allowed
    sentence = connectionSocket.recv(1024).decode()  #receive message 
    print(addr)
    print(sentence)
    print("Received message length:", len(sentence)) #print the lenghth of received message
    #connectionSocket.send(str(len(sentence)).encode()) # reply the length of the message
    capitalizedSentence = sentence.upper() # capitalization
    connectionSocket.send(capitalizedSentence.encode()) #reply the capitalized message to client
    connectionSocket.close() #close the connected socket
