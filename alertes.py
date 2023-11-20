# coding: utf-8
from tkinter import *
from tkinter.messagebox import *
fenetre = Tk()

fenetre.title("Talend")
fenetre['bg']='white'
def callback():
    if askyesno("titre1","etes vous sur de voiloire faire ça?"):
        showwarning("titre2", "tant pis...")
    else:
        showinfo('titre3','vous avez peur!')
        if askyesno('titre 33', 'il ne faut pas avoir peur'):
            showinfo('titre 333', 'bravo')
        else:
            showwarning('titre 44','lache')
            showerror("titre 4", "ahh")

Button(text='Action', command=callback()).pack()
fenetre.mainloop()