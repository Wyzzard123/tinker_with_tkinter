from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Title of this software")
root.iconbitmap('favicon.ico')

my_img = ImageTk.PhotoImage(Image.open("miku.png"))

my_label = Label(image=my_img)

my_label.pack()


button_quit = Button(root, text="Exit Program", command=root.quit)

button_quit.pack()


root.mainloop()