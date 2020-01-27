from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Title of this software")
root.iconbitmap('favicon.ico')

frame = LabelFrame(root, text="This is a frame...", padx=50, pady=50)

frame.pack(padx=100, pady=100)

b = Button(frame, text="Don't Click Here!")
b.grid(row=0, column=0)

b2 = Button(frame, text="...or here!")
b2.grid(row=1, column=1)

root.mainloop()