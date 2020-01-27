from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Title of this software")
root.iconbitmap('favicon.ico')

# r=IntVar()
# r.set("2")



MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W) # Use indicatoron=0 to get button boxes instead of radio buttons

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

# myLabel = Label(root, text=r.get())
# myLabel.pack()

# myButton = Button(root, text="Click me!", command=lambda: clicked(r.get()))
# myButton.pack()



myButton = Button(root, text="Click me!", command=lambda: clicked(pizza.get()))
myButton.pack()

mainloop()