import tkinter as tk
def displayLabel():
    label.configure(text="こんにちは")

root = tk.Tk()
root.geometry('200x100')

label = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH", command = displayLabel)

label.pack()
btn.pack()
tk.mainloop()