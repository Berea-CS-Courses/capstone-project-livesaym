import socket
import threading
from GUI import *
import sqlite3
import time
from google_trans_new import google_translator
import random

chat = start_gui()

output_box = start_output(chat)

input_box = start_input(chat)

HOST = '0.0.0.0'  # '10.16.4.104' (Internet) or '127.0.0.1'(Local machine for testing)
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
usernames = []

translator = google_translator()

id_num = 1  # For iterating ID number while saving to messages2 table

# conn = sqlite3.connect('database.db')

# cur = conn.cursor()


def test_func(client):
    client.send('Uzbfer'.encode('utf-8'))


def save_message(username, msg):
    print(username)
    print(msg)
    conn = sqlite3.connect('database.db')  # Access database.db
    cur = conn.cursor()  # Create cursor for accessing messages table
    params = (username, msg)
    cur.execute("INSERT INTO messages (username, message) VALUES (? , ?)", params)
    # ^Saves params (username, msg) to the 'messages' database, under columns (username, message)
    conn.commit()
    conn.close()
    print("Saved to messages")
    return


def translate_message(username, msg):
    potential_languages = ['de', 'ko', 'ja', 'la']
    chosen_language = random.choice(potential_languages)
    # print(potential_languages)
    translated_text = translator.translate(msg, lang_tgt=chosen_language)
    print(translated_text)
    combined_text = (username + ': ' + translated_text + '\n')
    return combined_text


def translate_and_save_message(username, msg):
    conn = sqlite3.connect('database.db')  # Access database.db
    cur = conn.cursor()  # Create cursor for accessing messages table
    potential_languages = ['de', 'ko', 'ja', 'la']
    chosen_language = random.choice(potential_languages)
    # print(potential_languages)
    translated_text = translator.translate(msg, lang_tgt=chosen_language)
    print(translated_text)
    params = ( username, msg, translated_text)
    print("Saving")
    cur.execute("INSERT INTO messages (id_number, username, message, translation) VALUES (NULL, ?, ?, ?)", params)
    conn.commit()
    conn.close()
    print("Saved to messages")
    combined_text = (username + ': ' + translated_text + '\n')
    return combined_text


def broadcast2(message):
    # Exists so when welcoming message gets broadcast, it won't get saved like regular messages
    print("Broadcast 2")
    for client in clients:
        client.send(message)


def broadcast_history(client):
    conn = sqlite3.connect('database.db')  # Access database.db
    cur = conn.cursor()  # Create cursor for accessing messages table
    time.sleep(1)  # Wait for client GUI to finish building
    for row in cur.execute("SELECT username, translation FROM messages "):
        current_row = row
        # print(current_row)
        username, message = current_row
        print(username + ': ' + message + '\n')
        combined_message = username + ': ' + message + '\n'
        client.send(combined_message.encode('utf-8'))


def broadcast(message):
    print(message)
    msg = message.decode('utf-8')
    print(msg)
    splitmsg = msg.split(':', 1)
    print(splitmsg)
    username = splitmsg[0]
    just_message = splitmsg[1]
    print("Translating")

    combined_text = translate_and_save_message(username, just_message)
    # save_message(username, just_message)
    print("Translated!")
    # print(translated_text)
    # print("Encoding")
    # combined_text = (username + ': ' + translated_text)
    print(combined_text)
    print("Broadcasting...")
    for client in clients:
        client.send(combined_text.encode())  # 'message' for original, 'translatedText' otherwise


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            # msg = message["data"].decode("utf-8")
            # print_output(chat, output_box, msg)
            # Save chat message
            print(f"{usernames[clients.index(client)]}")
            broadcast(message)  # 'message' for regular message, translatedText for translation
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

        if username in usernames:
            client.send("That username is already in use.".encode('utf-8'))
        else:
            usernames.append(username)
            clients.append(client)

            print(f"User connected")
            broadcast2(f"{username} connected to the server!\n".encode('utf-8'))
            client.send("Connected to server".encode('utf-8'))

            broadcast_history(client)

            thread = threading.Thread(target=handle, args=(client,))
            thread.start()


print(f'Listening for connections on {HOST}:{PORT}')
receive()
