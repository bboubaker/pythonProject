# coding: utf-8
from tkinter import *

fenetre = Tk()

fenetre.title("Talend")
fenetre['bg']='white'
p = PanedWindow(fenetre, orient=HORIZONTAL)
p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
p.add(Label(p, text='Volet 1', background='blue', anchor=CENTER))
p.add(Label(p, text='Volet 2', background='white', anchor=CENTER))
p.add(Label(p, text='Volet 3', background='red', anchor=CENTER))
p.pack()

fenetre.mainloop()