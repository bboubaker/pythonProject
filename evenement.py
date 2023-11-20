# coding: utf-8
import tkinter
from tkinter import *
from tkinter.filedialog import *

fenetre = Tk()
fenetre.title("formation python")

def clavier(event):
    touche = event.keysym
    print(touche)

canvas = Canvas(fenetre, width=500, height=500)
canvas.focus_set()
canvas.bind("<B1-Motion>", clavier)
canvas.pack()

fenetre.mainloop()