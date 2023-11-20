# coding: utf-8
from tkinter import *

fenetre = Tk()

fenetre.title("Talend")
fenetre.minsize(width=50, height=75)
fenetre.config(background='#E5E3D6')
fenetre.configure(padx=20, pady=20)

label = Label(fenetre,text="hello word", bg="yellow")
label.pack()

value = StringVar()
value.set("text par defaut")
entree = Entry(fenetre,textvariable=value, width=30)
entree.pack()

#bouton = Button(fenetre,text="Fermer",command=fenetre.quit)
#bouton.pack()

bouton2 = Checkbutton(fenetre, text="Nouveau?")
bouton2.pack()
value = StringVar()
bouton3 = Radiobutton(fenetre, text="OUI", variable=value,value=1)
bouton3.pack()
bouton4 = Radiobutton(fenetre, text="NON", variable=value,value=2)
bouton4.pack()
bouton5 = Radiobutton(fenetre, text="OUI/NON", variable=value,value=3)
bouton5.pack()

liste = Listbox(fenetre)
liste.insert(1,"python")
liste.insert(2,"php")
liste.insert(3,"data")
liste.pack()

canvas = Canvas(fenetre, width=150, height= 120, background="yellow")
ligne1 = canvas.create_line(75, 0,75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Talend",font="Arial 16 italic", fill="blue")
canvas.pack()

value = DoubleVar()
scale = Scale(fenetre,variable=value)
scale.pack()

fenetre.mainloop()

