import tkinter as tk
import tkinter.filedialog as fd
# image ライブラリー
from PIL import Image, ImageTk

def dispPhoto(path):
    newImage = Image.open(path).convert("L").resize((32,32)).resize((300,300))
    imageData = ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()

    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry('400x350')

btn = tk.Button(text="open file", command = openFile)
imageLabel = tk.Label()
"""
pack elements
"""
btn.pack()
imageLabel.pack()
tk.mainloop()