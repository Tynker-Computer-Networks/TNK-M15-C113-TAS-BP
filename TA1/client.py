import socket
from tkinter import *
from  threading import Thread
import random
from PIL import ImageTk, Image

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None
canvas1 = None

player_name = None
name_entry = None
name_window = None

def ask_player_name():
    global player_name, name_entry, name_window, canvas1
    name_window  = Tk()
    name_window.title("Ludo Ladder")

    # Use Image.open() to load the image in image variable
    
    # Use resize method on image to resize it to screen_width and screen_height
    
    # Use ImageTk.PhotoImage() to create a bg using image
    
    
    # Create a canvas on name_window of width and height of screen width and height
    
    # Use pack() method on canvas to cover all the screen space
    
    # Add image to canvas using create_image method
    
    # Use create_text() method to add text "Enter Name" 
    

    name_entry = Entry(name_window,  justify='center', font=('Chalkboard SE', 10), bd=5, bg='white')
    name_entry.place(relx = 0.25, rely=0.3, relwidth = 0.5)
    
    button = Button(name_window, text="Save", font=("Chalkboard SE", 10), height=1, bg="#80deea", bd=3)
    button.place(relx= 0.33, rely=0.5, relwidth = 0.34)

    name_window.resizable(True, True)
    name_window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 5000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    ask_player_name()

setup()
