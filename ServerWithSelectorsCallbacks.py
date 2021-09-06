import socket
import selectors

selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM == TCP
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    selector.register(fileobj = server_socket, events = selectors.EVENT_READ, data = acceptConnection)

def acceptConnection(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)
    
    selector.register(fileobj = client_socket, events = selectors.EVENT_READ, data = sendMsg)


def sendMsg(client_socket):
    print('Before receive')

    request = client_socket.recv(4096) # 4096 == buffer size

    if request:
        response = 'Hello\n'.encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket)
        client_socket.close()

def event_loop():
    while True:
       events = selector.select() # (key, events)

       # SelectorKey
       # fileObj
       # event
       # data

       for key, _ in events:
           callback = key.data
           callback(key.fileobj)

if __name__ == '__main__':
    server()
    event_loop()

