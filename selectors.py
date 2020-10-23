import socket
import selectors


selector = selectors.DefaultSelector()


def server():
    # SOCK_STREAM - поддержка протокола tcp
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Отключаем задержку по портам
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    selector.register(fileobj=server_socket, events=selectors.EVEBT_READ, data=accept_connection)


def accept_connection(server_socket):
        client_socket, addr = server_socket.accept()
        print('Connection addr ', addr)

        selector.register(fileobj=client_socket, events=selectors.EVEBT_READ, data=send_message)


def send_message(client_socket):

    request = client_socket.recv(4096)

    if request:
        response = '\nHello world!\r'.encode()  # Преобраовываем в bytes
        client_socket.send(response)
    else:
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    while True:

        events = selector.select()  # key, event

        # SelectorKey
        # fileobj
        # events
        # data

        for key, _ in events:
            callback = key.data     # get function (is inside attribute 'data')
            callback(key.fileobj)   # call function (fileobj - socket)

if __name__ == '__main__':
    server()
    event_loop()
