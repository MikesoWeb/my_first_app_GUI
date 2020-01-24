
from tkinter import *
import random

win = Tk()
win.title('My_prog_GUI')
win.geometry('500x250+150+150')


chars = 'xjvndu57476'


def generate_pass():
  
  #ent_text=textentry.get()
  output.delete(0.0,END)
  for i in range(12):
    password+= random.choice(chars)
  output.insert(0.0, password)
 



textentry = Entry(win, width = 20, bg = 'white')
textentry.grid(row=3, column=2)



output = Text(win, width=30,height=10, wrap = WORD, background='white')
output.grid(row=5, column=0)

Button(win, text='Submit',width=6,command = generate_pass) .grid(row=3,column=0,sticky=W)



win.mainloop()