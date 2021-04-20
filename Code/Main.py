import socket
import threading
from GUI import *
import goslate
import time

chat = start_gui()

output_box = start_output(chat)

input_box = start_input(chat)

HOST = '0.0.0.0' # '10.16.4.104' (Internet) or '127.0.0.1'(Local machine for testing)
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
usernames = []

gs = goslate.Goslate()

def broadcast(message):
    #print("Decoding")
    #msg = message["data"].decode("utf-8")
    #print_output(chat, output_box, msg)
    #print(message)
    # print("Translating")
    # time.sleep(5) # Sleep is supposed to prevent 'HTTP Error 429: Too Many Requests' from appearing, but is inconsistent
    # translatedText = gs.translate(message,'fr') # Translation based og goslate module. Comment line out if Error 429 happens, to work on other aspects
    # print("Translated!")
    # print(translatedText)
    # print("Encoding")
    # translatedText.encode()
    # print(translatedText)
    print("Broadcasting...")
    for client in clients:
        client.send(translatedText) # 'message' for original, 'translatedText' otherwise

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(message)
            #msg = message["data"].decode("utf-8")
            #print_output(chat, output_box, msg)
            #Save chat message
            print(f"{usernames[clients.index(client)]}")

            broadcast(message) # message for regular message, translatedText for translation
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            usernames.remove(username)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}!")

        client.send("Username?".encode('utf-8'))
        username = client.recv(1024)

        usernames.append(username)
        clients.append(client)

        print(f"User connected")
        broadcast(f"{username} connected to the server!\n".encode('utf-8'))
        client.send("Connected to server".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print(f'Listening for connections on {HOST}:{PORT}')
receive()
