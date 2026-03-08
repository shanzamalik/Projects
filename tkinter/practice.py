from tkinter import *
s_root= Tk()

#width*height
s_root.geometry("644x434")
#width,heigth
s_root.minsize(300,100)
s_root.maxsize(1200,988)


label1=Label(text="zarwa is a good girl.i love her.",fg="light green",background="YELLOW",font="Helvic 16 bold italic")
label1.pack()

#gui logic here.
#show gui window on screen
s_root.mainloop()

#733*434(pycharm screen approx)