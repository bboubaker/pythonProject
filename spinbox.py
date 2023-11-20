# coding: utf-8
from tkinter import *

fenetre = Tk()

fenetre.title("Talend")
fenetre['bg']='white'

l = LabelFrame(fenetre, text="open the file", padx=20, pady=20)
l.pack(fill="both", expand="yes")
Label(l, text="text a l'interieur de frame").pack()
s = Spinbox(l, from_=0, to=10)
s.pack()


fenetre.mainloop()