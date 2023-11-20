# coding: utf-8
import tkinter
from tkinter import *
from tkinter.messagebox import *
#from PIL import Image

from alert import alert

ma_fenetre = Tk()
ma_fenetre.title("formation python")




def rec():
    showinfo("alerte", entree.get())

value = StringVar()
value.set("Valeur")
entree = Entry(ma_fenetre, textvariable=value, width=30)
entree.pack()

bouton = Button(ma_fenetre, text="valider", command=rec())
bouton.pack()








fenetre.mainloop()