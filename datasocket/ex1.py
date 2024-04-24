from socket import *  # 소켓 프로그래밍을 위한 모듈 가져오기
import sys  # 시스템 관련 기능을 사용하기 위한 모듈

# TCP 서버 소켓 생성
serverSocket = socket(AF_INET, SOCK_STREAM)

# 서버 주소와 포트를 소켓에 바인딩
serverPort = 80  # 서버 포트 설정
serverSocket.bind(('localhost', serverPort))  # localhost 주소에 바인드

# 동시에 하나의 연결만 수신하도록 리스닝
serverSocket.listen(1)

print('The server is ready to receive')  # 서버 준비 완료 메시지 출력

# 무한 루프를 돌면서 클라이언트의 연결 요청 대기
while True:
    connectionSocket, addr = serverSocket.accept()  # 클라이언트 연결 수락

    try:
        message = connectionSocket.recv(1024).decode()  # 클라이언트로부터 메시지 수신 및 디코드
        print(message)
        filename = message.split()[1]  # HTTP 요청으로부터 파일 이름 추출
        with open(filename[1:], 'rb') as f:  # 요청된 파일 오픈 (바이너리 모드)
            outputdata = f.read()  # 파일의 모든 데이터 읽기
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())  # HTTP 200 OK 응답 헤더 전송
            connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())  # 컨텐트 타입 헤더 전송
            connectionSocket.send(outputdata)  # 파일 데이터 전송
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())  # 파일이 없을 경우 404 에러 전송
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())  # 컨텐트 타입 헤더 전송
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())  # 404 에러 페이지 내용 전송
    finally:
        connectionSocket.close()  # 클라이언트 소켓 닫기

serverSocket.close()  # 서버 소켓 닫기
sys.exit()  # 프로그램 종료
