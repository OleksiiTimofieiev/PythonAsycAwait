import socket
from select import select

toMonitor=[]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM == TCP
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

def acceptConnection(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    toMonitor.append(client_socket)

def sendMsg(client_socket):
        print('Before receive')

        request = client_socket.recv(4096) # 4096 == buffer size

        if request:
            response = 'Hello\n'.encode()
            client_socket.send(response)
        else:
            client_socket.close()

def event_loop():
    while True:
        readyToRead, _, _ = select(toMonitor, [], []) #read, write, errors

        for sock in readyToRead:
            if sock is server_socket:
                acceptConnection(sock)
            else:
                sendMsg(sock)

if __name__ == '__main__':
    toMonitor.append(server_socket)
    event_loop()

