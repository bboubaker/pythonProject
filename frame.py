# coding: utf-8
from tkinter import *

fenetre = Tk()

fenetre.title("Talend")
#fenetre.minsize(width=50, height=75)
#fenetre.config(background='#E5E3D6')
#fenetre.configure(padx=20, pady=20)

Frame1 = Frame(fenetre, borderwidth=2, relief="groove")
Frame1.pack(side=LEFT, padx=30, pady=30)
Label(Frame1, text="FRAME 1").pack(padx=10, pady=10)

frame2 = Frame(fenetre, borderwidth=2, relief="groove")
frame2.pack(side=LEFT, padx=10, pady=10)
Label(frame2, text="FRAME 2").pack(padx=10, pady=10)

frame3 = Frame(frame2, bg="white", borderwidth=2, relief="groove")
frame3.pack(side=RIGHT, padx=5, pady=5)
Label(frame3, text="Frame 3", bg="white").pack(padx=10,pady=10)


fenetre.mainloop()

