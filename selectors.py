import socket
import selectors


selector = selectors.DefaultSelector()

# SOCK_STREAM - поддержка протокола tcp
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Отключаем задержку по портам
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()


def accept_connection(server_socket):
        client_socket, addr = server_socket.accept()
        print('Connection addr ', addr)


def send_message(client_socket):

    request = client_socket.recv(4096)

    if request:
        response = '\nHello world!\r'.encode()  # Преобраовываем в bytes
        client_socket.send(response)
    else:
        client_socket.close()


def event_loop():
    while True:

        pass

if __name__ == '__main__':
    event_loop()
