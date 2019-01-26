##########################
#                        #
# MY FIRST PYTHON POJECT #
#      AUDIO PLAYER      #
#                        #
##########################

#importing the tkinter module
import tkinter as tk
from tkinter import *
import mutagen
from mutagen import *
import pygame
from pygame import *

#keypress function
def click():
    searched=search.get()
#creating a tkinter window
main = tk.Tk()
main.title('Smart Player')
main.configure(background="#3FA9F5")
main.iconbitmap(r'icon.ico')
##creating menu functions
def openmusic():
    print('I will open when you define me well')

def openfolder():
    print('I will open when you define me well')
   
def close_window():
    main.destroy()
    exit()

def help():
    print('version 1.1.1')
    print ('developed by Samizzo Gekworldke')
#3. creatinf a top ribbon menu bar
menu= Menu(main)

main.config(menu=menu)

#dropdown submenu
submenu= Menu(menu)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open Music file", command=openmusic)
submenu.add_command(label="Open Folder", command=openfolder)
submenu.add_command(label="Exit", command=close_window)
#2
menu.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="Open Music file", command=openmusic)

#2. creating a label
Label (main, text="Smart Audio Player", bg="white", fg="red") .grid(row=1, column=0, sticky=W)

#create a text entry box
search= Entry(main, width=40, bg="gray")
search.grid(row=1, column=1, sticky=E)

#submit button
Button (main, text="SEARCH", width=6, command=click) .grid(row=1, column=3, sticky=E)

##display canvas

#control functions
def Play():
    print("Soon I will play")

def Pause():
    print("Soon I will pause your music")

def Stop():
    print("Soon I will stop your music")
#control buttons
fm = Frame(main)
play= Button(fm, text="Play", command=Play) .pack(side=LEFT) 
pause= Button(fm, text="Pause", width=14, command=Pause) .pack(side=LEFT)
stop= Button(fm, text="Stop", width=14, command=Stop).pack(side=LEFT)
fm.pack()


#run the output

main.mainloop()
