Link to Google Doc: https://docs.google.com/document/d/1KdPiWUIiBVbnctXdIBG65aY9rqDZiaLgoYdSAxxMXx0/edit


Matthew Livesay
Project Decomposition Document

# Translating Chat App
Components in Descending Order of Importance:
 - Networking infrastructure/code
   - Host/Server
     - Where all clients connect to
     - Stores chat messages
   - Client
     - Connects to host
     - Has unique username
   - At log-in page, users select if they want to start or join a chat server
     - This should make it easier for a single executable to work for both hosts and clients.
   - Python sockets
     - Low level network library
 - User Interface
   - Log-in Screen
     - User chooses to start or join chat room
     - Sign-up prompt for those without user info
   - Chat log
     - Main chatroom
       - Multi-user, anyone can see any message
     - Personal message
       - One-on-one
     - Displays original message at first; Once translation functionality is built, then display translated message w/o original message
     - Stretch goal: Add button on message display for users to press that will display original, untranslated message.
   - Python tkinter
     - UI code shouldn’t be too closely intertwined w/ netcode; can cause slowdowns/freezes
 - Chat Log Database
   - Original chat message
   - Translated chat message
     - Make spots for this even before translation is implemented; Probably easier in the long run
   - Sender’s username
   - Receiver
     - Username of PM receiver OR
   - Main chatroom
     - Is attached to host/server
     - Cleared if host shuts down server
     - Shouldn’t be visible to other servers
     - Max amount of stored messages 
       - Prevents potential storage issues
       - Extremely old messages might be less relevant
   - Python MySQL
 - User Info Database
   - Username
     - Must be unique; Checks if specified username already exists at account creation
   - Password
     - Having requirements like “Must be x length” and “Must contain a number, symbol, and vowel” could be stretch goals
     - Stored separately from host or client
       - Shouldn’t be cleared when server shuts down
       - Should be used by all servers
   - Stretch goal: Deletes user info if they do not log after set amount of time
   - Python MySQL
 - Translation Algorithm
   - Input: English
   - Output: Different language or expression method
     - Examples: Spanish, emojis, numbers
   - At least one non-English option, more optional
     - Slices messages into sets strings, detects if word is in english, translates random word(s), reassembles message
       - “Random” is tentative; Could be every third word, the exact middle and ends of messages, etc.
   - Python translate OR Google translate/googletrans and pandas

minor change

