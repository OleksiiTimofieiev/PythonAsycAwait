import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM == TCP
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

while True:
    print('Before accept')
    client_socket, addr = server_socket.accept()

    print('Connection from', addr)

    while True:
        print('Before receive')

        request = client_socket.recv(4096) # 4096 == buffer size

        if not request:
            break
        else:
            response = 'Hello\n'.encode()
            client_socket.send(response)

