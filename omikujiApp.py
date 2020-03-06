import tkinter as tk
import random

def displayLabel():
    kuji = ['大吉', '小吉', '中吉', '吉']
    label.configure(text=random.choice(kuji))

root = tk.Tk()
root.geometry('200x100')

label = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH", command = displayLabel)

label.pack()
btn.pack()
tk.mainloop()