# coding: utf-8
import tkinter
from tkinter import *
from tkinter.messagebox import *
#from PIL import Image

from alert import alert

fenetre = Toplevel()

fenetre.title("formation python")
photo = PhotoImage(file="C:/Users/bahi_/PycharmProjects/pythonProject/im.png")
canvas = Canvas(fenetre, width=1350, height=1250)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()

fenetre.mainloop()