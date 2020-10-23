import socket

# SOCK_STREAM - поддержка протокола tcp
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Отключаем задержку по портам
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()


def accept_connection(server_socket):
    while True:
        client_socket, addr = server_socket.accept()
        print('Connection addr ', addr)


def send_message(client_socket):
    while True:
        print('Before .recv()')
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = '\nHello world!\r'.encode()  # Преобраовываем в bytes
            client_socket.send(response)

    client_socket.close()


if __name__ == '__main__':
    accept_connection(server_socket)
