### Overview
The project that I am making is a discord-like chatting computer program for desktop and laptop computers that translates parts of your message to a different language.
People will be able to chat in real time with others who connect to the program and see previous messages from other people. The point of this program is to see how people's
communication is changed by making the communication more opaque in ways the subject can't control, as well as to challenge myself as a programmer and try to expand my
skillset.

### Concept
This program is a discord style chatting application for desktop and laptop computers written in Python. Users should be able to log in with their username and connect with
other users. User names may or may not require a password to access and may or may not be unique to each user. Users should be able to send text messages between each other and
view previous messages that were sent by themselves or the user that they are communicating with. Messages sent by users should have a part of it translated into a language
other than english, or into some other form that makes it difficult to understand. This can include emojis or numbers. It will be assumed that users primary language will be
english.

### Software Requirement Specifications
1. The program will need to be able to run on Windows 10
2. This program will utilize the sockets library to maintain online functionality
3. This program tkinter or a similar user intergace library to provide users with a GUI for them to interact with and type messages into
4. There will need to be a database made for previous messages from users going back to a certain point (for example, this may only store the last 100 messages made with the
program) which will include the original message, the modified message, and who sent it. 
5. There will also be a database for users, which will include usernames and potentially passwords users so they can log in. 
6. There will need to be some sort of translation library to translate messages from english to whatever other language or form the messages might be in.
