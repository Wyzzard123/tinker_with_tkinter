from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Title of this software")
root.iconbitmap('favicon.ico')

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday",
    "Saturday"
]
clicked = StringVar()
clicked.set(options[0])


drop = OptionMenu(root, clicked, *options).pack() # You can also type the options one by one like OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday"...) but this way is much easier to edit later on

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()