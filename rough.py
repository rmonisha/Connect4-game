from tkinter import *
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import os


def start_game():
    os.system('python connect4_game.py')

def leave_game():
    return win.destroy()

win=Tk()
win.title('Connect4')
win.geometry("700x350")
win['background']='#bdffeb'

frame=Frame(win,bg='#bdffeb')
frame.pack(expand=True, fill=BOTH)


label=Label(win, bg='#bdffeb',text=" Steps to play Connect4\n\nThe player is assigned red and the AI yellow\nPlayers drop the coins alternatively\nThe first one to get four coins in a row wins ", font='Arial 17 bold',justify='left')
label.place(relx=0.5, rely=0.5, anchor=CENTER)

button1 = Button (win,text='START', command = start_game,bg ='#00e699',fg='#ffffff',activebackground='#ff66ff' ,font= 'Times 20')
button1.pack(side=RIGHT)

button2 = Button (win,text = 'QUIT',command = leave_game,bg ='#00e699',fg='#ffffff',activebackground='#ff66ff',font= 'Times 20')
button2.pack(side=LEFT)

win.mainloop()
