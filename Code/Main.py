import socket
import threading
from GUI import *
import goslate
import sqlite3

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

conn = sqlite3.connect('database.db')

cur = conn.cursor()


def save_message(username, msg):
    print(username)
    print(msg)
    conn = sqlite3.connect('database.db') # Access database.db
    cur = conn.cursor() # Create cursor for accessing messages table
    params = (username, msg)
    cur.execute("INSERT INTO messages (username, message) VALUES (? , ?)", params)
    # ^Saves params (username, msg) to the 'messages' database, under columns (username, message)
    conn.commit()
    conn.close()
    print("Saved to messages")
    return


def broadcast2(message): # Exists so when welcoming message gets broadcast, it won't get saved like regular messages
    print("Broadcast 2")
    for client in clients:
        client.send(message)


def broadcast(message):
    print(message)
    print("Decoding")
    msg = message.decode('utf-8')
    print(msg)
    splitmsg = msg.split(':', 1)
    print(splitmsg)
    username = splitmsg[0]
    justMessage = splitmsg[1]
    save_message(username, justMessage)
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
        client.send(message) # 'message' for original, 'translatedText' otherwise


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            #msg = message["data"].decode("utf-8")
            #print_output(chat, output_box, msg)
            #Save chat message
            print(f"{usernames[clients.index(client)]}")
            broadcast(message) # 'message' for regular message, translatedText for translation
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
        broadcast2(f"{username} connected to the server!\n".encode('utf-8'))
        client.send("Connected to server".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print(f'Listening for connections on {HOST}:{PORT}')
receive()
