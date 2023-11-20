# coding: utf-8
from tkinter import *
from tkinter.messagebox import *


from alert import alert

fenetre = Tk()

fenetre.title("Talend")


Canvas(fenetre, width=250, height=50, bg='ivory').pack(side=LEFT, padx=5, pady=5)
Button(fenetre, text='bouton 1', cursor='watch').pack(side=TOP,  padx=5, pady=5)
Button(fenetre, text='bouton 2', cursor='circle').pack(side=BOTTOM, padx=5, pady=5)

fenetre.mainloop()