# coding: utf-8
from tkinter import *
from tkinter.messagebox import *


from alert import alert

fenetre = Tk()

fenetre.title("Talend")

Button(fenetre, text='L1-C1', borderwidth=1).grid(row=1, column=1)
Button(fenetre, text='L1-C2', borderwidth=1).grid(row=1, column=2)
Button(fenetre, text='L2-C3', borderwidth=1).grid(row=2, column=3)
Button(fenetre, text='L2-C4', borderwidth=1).grid(row=2, column=4)
Button(fenetre, text='L3-C3', borderwidth=1).grid(row=3, column=3)

#for ligne in range(5):
#    for colonne in range(5):
#        Button(fenetre, text='L%s-C%s' % (ligne, colonne), borderwidth=2).grid(row=ligne, column=colonne)


fenetre.mainloop()