from tkinter import *
from math import *


def evaluate(event):
    res.configure(text='Ergebnis: '+str(eval(entry.get())))

w = Tk()
Label(w, text='Your Expression:').pack()
entry = Entry()
entry.bind('<Return>', evaluate)
entry.pack()
res = Label(w)
res.pack()
w.mainloop()
