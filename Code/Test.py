# Just for tests
# Don't upload
import sqlite3  # MySQL doesn't want to work, so I'm switching to SQLite3
import time
import random
from google_trans_new import google_translator

# text = ["Hello", "Greetings", "What", "is", "up", "dog"]
# username = "Matthew"
# finished_text = [':', ' ']
# translator = google_translator()
# for i in text:
#     potential_languages = ['de', 'ko', 'ja', 'la']
#     chosen_language = random.choice(potential_languages)
#     print(i)
#     translate_text = translator.translate(i, lang_tgt=chosen_language)
#     print(translate_text)
#     finished_text.append(translate_text)


# class StoredMessage:
#     """
#     A class for more effectively using the sqlite3 database
#     """
#
#     def __init__(self, id_number, username, message, translation):
#         self.id_number = id_number()
#         self.username = username()
#         self.message = message()
#         self.translation = translation()


conn = sqlite3.connect('database.db')

cur = conn.cursor()
# cur.execute("DROP TABLE messages3")

# Three " means docstring, so multi-line commands can be made
# cur.execute("""CREATE TABLE messages
#     (id_number integer primary key autoincrement, username text, message text, translation text)""")
# ^ Makes table (Delete after first use I think)

# cur.execute("INSERT INTO messages VALUES (NULL, 'Matthew', 'Hello world', 'Bonjour le monde')")
# cur.execute("INSERT INTO messages VALUES (NULL, 'Matthew', 'Hello', 'Bonjour') ")
# ^ Inserts into the table the stated values, in column order specified above

for row in cur.execute("SELECT * FROM messages"):
    print(row)
# conn.commit()  # Saves changes
# conn.close()  # Closes connection

# import socket
# import threading
# import tkinter
# import tkinter.scrolledtext
# from tkinter import simpledialog
#
# HOST = '127.0.0.1'  # Can be '127.0.0.1' (Local machine for testing) or use ipcofig in command line on server
# # machine for IP
# PORT = 9090
#
#
# class Client:
#
#     def __init__(self, host, port):
#         self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.sock.connect((host, port))
#
#         msg = tkinter.Tk()
#         msg.withdraw()
#
#         self.nickname = simpledialog.askstring("Log In", "Please choose a username", parent=msg)
#
#         self.gui_done = False
#         self.running = True
#
#         gui_thread = threading.Thread(target=self.gui_loop)
#         receive_thread = threading.Thread(target=self.receive)
#
#         gui_thread.start()
#         receive_thread.start()
#
#     def gui_loop(self):
#         self.win = tkinter.Tk()
#         self.win.config(bg="blue")
#
#         self.chat_label = tkinter.Label(self.win, text="Chat:", bg="blue")
#         self.chat_label.config(font=("Arial", 12))
#         self.chat_label.pack(padx=20, pady=5)
#
#         self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
#         self.text_area.pack(padx=20, pady=5)
#         self.text_area.config(state='disabled')
#
#         self.msg_label = tkinter.Label(self.win, text="Message:", bg="blue")
#         self.msg_label.config(font=("Arial", 12))
#         self.msg_label.pack(padx=20, pady=5)
#
#         self.input_area = tkinter.Text(self.win, height=1)
#         self.input_area.pack(padx=20, pady=5)
#
#         self.send_button = tkinter.Button(self.win, text="Send", command=self.write)
#         self.send_button.config(font=("Arial", 12))
#         self.send_button.pack(padx=20, pady=5)
#
#         self.gui_done = True
#
#         self.win.protocol("WM_DELETE_WINDOW", self.stop)
#
#         self.win.mainloop()
#
#     def write(self):
#         message = f"{self.nickname}: {self.input_area.get('1.0', 'end')}"
#         self.sock.send(message.encode('utf-8'))
#         self.input_area.delete('1.0', 'end')
#
#     def stop(self):
#         self.running = False
#         self.win.destroy()
#         self.sock.close()
#         exit(0)
#
#     def receive(self):
#         while self.running:
#             try:
#                 message = self.sock.recv(1024).decode('utf-8')
#                 print(message)
#                 if message == 'Username?':
#                     self.sock.send(self.nickname.encode('utf-8'))
#                 elif message == 'That username is already in use.':
#                     print("Please restart and try again")
#                     continue
#                 else:
#                     if self.gui_done:
#                         self.text_area.config(state='normal')
#                         self.text_area.insert('end', message)
#                         self.text_area.yview('end')
#                         self.text_area.config(state='disabled')
#
#             except ConnectionAbortedError:
#                 break
#             except:
#                 print("Oh no!")
#                 self.sock.close()
#                 break
#
#
# client = Client(HOST, PORT)
