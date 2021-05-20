import tkinter
from tkinter import *


class MyGUI(tkinter.Frame):
    """
    A class for the graphical user interface.
    Developed with hopes that it'll fix 'Not Responding' issue.
    Will be run on different thread.
    Currently a work-in-progress.
    """
    def __init__(self):
        tkinter.Frame.__init__(self)
        self.window = tkinter.Tk()
        self.window.pack()
        self.window.Title("Chat Application (Server)")
        self.output_text = tkinter.Text(self.window, wrap=WORD, justify=LEFT)
        self.output_text.pack()
        self.input_box = tkinter.Entry(self.window, justify=LEFT)
        self.input_box.pack()
        self.send = tkinter.Button(self.window, text='SEND', command=self.send_input)

    def output(self, msg):
        self.output_text.insert(tkinter.END, "\n" + msg)
        self.output_text.update()
        self.window.update()

    def send_input(self):
        pass


__all__ = ["start_gui", "start_output", "start_input", "print_output"]


def start_gui():
    chat = tkinter.Tk()
    #chat.pack() # Tutorial said this was necessary to make GUI elements functional, but only works w/o it
    chat.title("Chat Application")
    return chat


def start_output(chat):
    output_box = tkinter.Text(chat, wrap=WORD, width=50)
    output_box.pack()
    chat.update()
    output_box.insert(tkinter.END, "Welcome!")
    return output_box


def start_input(chat):
    input_box = tkinter.Entry(chat, justify=LEFT)
    input_box.pack()
    chat.update()
    return input_box


def print_output(chat, output_box, msg):
    output_box.insert(tkinter.END, '\n' + msg)
    output_box.update()
    chat.update()


def login_screen():
    pass


def main():
    pass


if __name__ == "__main__":
    chat = start_gui()
    output_box = start_output(chat)
    input_box = start_input(chat)
    chat.mainloop()

    main()
