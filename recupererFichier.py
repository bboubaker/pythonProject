# coding: utf-8
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

fenetre = Tk()
fenetre.title("formation python")

filename = askopenfilename(title="Ouvrir une image", filetypes=[('txt files', '.txt'), ('all files', '.*')])

fichier = open(filename, "r")
content = fichier.read()
fichier.close()

Label(fenetre, text=content).pack(padx=10, pady=10)


fenetre.mainloop()