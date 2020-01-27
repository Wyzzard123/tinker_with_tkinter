from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Title of this software")
root.iconbitmap('favicon.ico')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check this box!", variable=var, onvalue="On", offvalue="Off")
c.deselect() # If you do not deselect, it starts selected by default
c.pack()

myButton = Button(root, text="Show selection", command=show).pack()
root.mainloop()