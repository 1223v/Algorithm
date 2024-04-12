from socket import *
serverName = '1.224.174.77' #myWorkstation is at a remote site in D318
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("Input lowercase sentence:")
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print("From Server:", modifiedSentence.decode())
clientSocket.close()
