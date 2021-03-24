import socket

import select

from GUI import *


# GUI information

chat = start_gui()

output_box = start_output(chat)

input_box = start_input(chat)

# Socket information for the server
headersize = 10
IP = "127.0.0.1"
PORT = 1234
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]
clients = {}
print(f'Listening for connections on {IP}:{PORT}')


#This lets program receive messages from clients
def receive_message(client_socket):
    try:
        message_header = client_socket.recv(headersize)

        if not len(message_header):
            return False
        message_length = int(message_header.decode('utf-8').strip())
        return{'header': message_header, 'data': client_socket.recv(message_length)}
    except: #Something went wrong
        return False


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            user = receive_message(client_socket)
            if user is False:
                continue

            sockets_list.append(client_socket)
            clients[client_socket] = user
            msg = '\n' + 'Accepting new connection from {} : {}, username: {}'.format(*client_address, user['data'].decode('utf-8'))
            print('Accepting new connection from {} : {}, username: {}'.format(*client_address, user['data'].decode('utf-8')))
            print_output(chat, output_box, msg)
        else:
            message = receive_message(notified_socket)
            if message is False:
                print('Closed connection from: {}'.format(*client_address, user['data'].decode('utf-8')))
                msg = '\n' + 'Closed connection from: {}'.format(*client_address, user['data'].decode('utf-8'))
                # client_address and user are actually defined by socket
                # Error is false positive; won't crash program
                print_output(chat, output_box, msg)
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]

            msg = f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}'
            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')
            print_output(chat, output_box, msg)
            # ^ Attempting to just have everyting print to GUI instead of console

            for client_socket in clients:

                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:

        sockets_list.remove(notified_socket)
        del clients[notified_socket]

