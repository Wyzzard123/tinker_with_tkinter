from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Title of this software")
root.iconbitmap('favicon.ico')

def open():
    global my_img # If not global, my_img does nothing
    top = Toplevel()
    top.title("Top window")
    top.iconbitmap('favicon.ico')

    my_img = ImageTk.PhotoImage(Image.open("billy2.png"))
    lbl = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()



root.mainloop()