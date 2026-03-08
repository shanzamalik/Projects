from tkinter import *
from PIL import Image, ImageTk

s_root=Tk()

s_root.geometry("933x734")
s_root.minsize(300,100)
s_root.maxsize(700,300)


img = Image.open("b1.png")#Open with Pillow
photo = ImageTk.PhotoImage(img) #Convert for Tkinter

image_label=Label(s_root,image=photo)
image_label.pack()

s_root.mainloop() 