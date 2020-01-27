from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Title of this software")
root.iconbitmap('favicon.ico')
root.geometry("400x400")

def slide():
    dimensions = f"{horizontal.get()}x{vertical.get()}"
    my_label = Label(root, text=dimensions).pack()
    root.geometry(dimensions)

vertical = Scale(root, from_=0, to=400) # You can also type command=slide here to make it scale while you slide, but it's really janky. If you do, slide needs to be defined as slide(var)
vertical.set(400)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.set(400)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()


    

my_btn = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()