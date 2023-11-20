# coding: utf-8
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

fenetre = Toplevel()
fenetre.title("formation python")

filepath = askopenfilename(title="Ouvrir une image", filetypes=[('png files', '.png'), ('all files', '.*')])
#print(filepath)

photo = PhotoImage(file=filepath)

canvas = Canvas(fenetre, width=photo.width(), height=photo.height(), bg="yellow")
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()

fenetre.mainloop()