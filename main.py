
from tkinter import *

win = Tk()
win.title('My_prog_GUI')
win.geometry('500x250+150+150')

def generate_pass():
  ent_text=textentry.get()
  output.delete(0.0,END)
  output.insert(0.0, ent_text)
 



textentry = Entry(win, width = 20, bg = 'white')
textentry.grid(row=3, column=4)



output = Text(win, width=75,height=30, wrap = WORD, background='white')
output.grid(row=5, column=0)

Button(win, text='Submit',width=6,command = generate_pass) .grid(row=3,column=0,sticky=W)



win.mainloop()