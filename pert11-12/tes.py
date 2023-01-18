import tkinter as tk 
import os

HEIGHT =  700 
Width = 800


root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT , width = Width)
canvas.pack()


base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'seed.png')
background_image=tk.PhotoImage(file = image_path)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()