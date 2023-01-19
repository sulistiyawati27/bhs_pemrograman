import tkinter as tk

def on_button_click():
    label.config(text="Hello, Sulistiyawati!")

root = tk.Tk()
root.title("Contoh GUI dengan Tkinter")

button = tk.Button(root, text="Klik Saya", command=on_button_click)
button.pack()

label = tk.Label(root)
label.pack()

root.mainloop()
