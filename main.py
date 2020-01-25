# -*- coding: utf-8 -*-

from pyperclip import copy
from tkinter import *
import random

win = Tk()
win.title('Генератор паролей 2020')
win.geometry('400x200+150+150')

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


def generate_pass():
    in_text = textentry.get()

    password = ''
    output.delete(0.0, END)
    for i in range(0, int(in_text)):
        password += random.choice(chars)
    c = str(output.insert(0.0, password))
    copy(c)


Label(text="Размер пароля:").grid(row=0, column=0)

textentry = Entry(win, width=10, bg='white')
textentry.grid(row=1, column=0)

output = Text(win, width=47, height=10, wrap=WORD, background='white')
# output.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
output.place(x=10, y=50)

Button(win, text='Генерировать', width=10, command=generate_pass).place(x=280, y=10)

win.resizable(width=False, height=False)

win.mainloop()
