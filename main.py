import socket

# SOCK_STREAM - поддержка протокола tcp
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Отключаем задержку по портам
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
server_socket.bind(('local_host', 6000))
server_socket.listen()

while True:
    print('Before .accept()')
    client_socket, addr = server_socket.accept()
    print('Connection addr ', addr)

    while True:
        print('Before .recv()')
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello world!\n'.encode()  # Преобраовываем в bytes
            client_socket.send(response)
