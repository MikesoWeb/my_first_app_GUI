# -*- coding: utf-8 -*-

from pyperclip import copy
from tkinter import *
import random

win = Tk()
win.title('Генератор паролей 2020')
win.geometry('500x250+150+150')

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


def generate_pass():
    in_text = textentry.get()

    password = ''
    output.delete(0.0, END)
    for i in range(0, int(in_text)):
        password += random.choice(chars)
    c = str(output.insert(0.0, password))
    copy(c)
    #passwrd = password
    #copy(passwrd)  # -- не работает на веб IDE


textentry = Entry(win, width=20, bg='white')
textentry.grid(row=3, column=2)

output = Text(win, width=50, height=10, wrap=WORD, background='white')
output.grid(row=5, column=0)

Button(win, text='Генерировать', width=10, command=generate_pass).grid(row=3, column=0, sticky=W)

win.mainloop()
