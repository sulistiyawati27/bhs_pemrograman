import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
import os

root = Tk()
root.title = ("sample app")


canvas = tk.Canvas(root, height = 400 , width = 580)
canvas.pack()

def beriair():
    showinfo(title='info', message='sudah di beri air')

def beripupuk():
    showinfo(title='info', message='sudah di beri pupuk')

#button air
base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'seed.png')
air=tk.PhotoImage(file = image_path)
button_air = Button(root,borderwidth=0, image=air, cursor="hand2", command=beriair)
button_air.place(x=10, y=10)

#button pupuk
base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'small.png')
pupuk=tk.PhotoImage(file = image_path)
button_pupuk = Button(root,borderwidth=0, image=pupuk, cursor="hand2", command=beripupuk)
button_pupuk.place(x=200, y=10)

#button pupuk
base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'iconair.png')
keluar=tk.PhotoImage(file = image_path)
#keluar = PhotoImage(file="iconair.png")
button_keluar = Button(root,borderwidth=0, image=keluar, cursor="hand2",command=root.destroy)
button_keluar.place(x=25, y=200)



root.mainloop()