Proof of Concept  
![Screenshot](https://github.com/Berea-CS-Courses/capstone-project-livesaym/blob/D4_Proof-of-Concept/Deliverables/images/Capstone_D4_Progress_1.PNG)  
A screenshot of me running the main and client scripts in Pycharm.  

Concept Documentation  
The proof-of-concept as it exists requires the installation of the Pycharm program, the most up-to-date version of Python, and the sockets and tkinter libraries. 
In order to run the proof-of-concept, you simply need to open the files in pycharm, run the “main” file, and then run the “client” file. The result is a GUI that
displays messages sent by the client to the server, as well as the username of the client. Unfortunately, the program has an issue with not responding after 
starting. Portions of the socket code in the server were taken from Stack Overflow. As for external tools, one would need a computer with the Windows 10 operating system on it and an internet connection, as well as the most up-to-date community version Pycharm and Anaconda. The modules being used so far include sockets, tkinter, select, errno, and sys. I will most likley also end up using other modules such a json or an equivalent data handling module, the threading module, and the goslate module, which connects to Google's translation API. Beyond that, I don't beleive that I will need any external dependencies. As far as I can tell, everything that I want to do with this project can be done with those tools, although there is always the possibility that I missed something.

Further Implementation
Now that I have the basics of sockets and sending messages implemented, I hope to begin putting together a user interface for the client using the tkinter module. After that, I will need to begin using the json module to start saving messages into a database, which will give me some experience with building databases and having them be manipulated via tkinter GUI inputs. After that, I would want to start to attempt to implement the translation module, which will have to interact with the messages as they get stored in a database and would also require some modification to the database. The next step after that would be to

Code
The code for the server creates a server socket and a list that will store the names of clients, and then defines a function for how to handle messages received
from a client. Then, in a while true loop, it listens for any incoming connections and binds them to a socket while appending the list of clients. When the while true
loop reveives a message from a connected client, it then decodes the data, prints the message and who its from in plaintext, and then sends it out to all other connected clients. The client code sets up its own sockets and then asks for a username. After the user puts one in, the code then starts a while true loop in which it will wait for any message that the user inputs and then encodes and sends it to the server. There is also code that will end the script if it detects and error, so it won't freeze up of something unexpected happens.

The functionality of the code is mostly restricted to the sockets and user interface, and is thus somewhat limited compared to what I want to make it into by the end of this semester. The user interface and log in feature is basic and the translation capabilities is nonexistent. 

Reflection  
Now that I’ve created a working proof of concept, I feel a bit more confident in my ability to complete the project. One of the things that I thought was going
to be one of the larger stumbling blocks was understanding sockets and how to implement them, since I haven't taken a class on them and they seemed very
complicated. Now that I have implemented a working version of python sockets, I feel much more confident. As for what I think I’ll need help with, integrating
different parts of the project, such as user interface and translation. 
