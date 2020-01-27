from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Title of this software")
root.iconbitmap('favicon.ico')


def open():
    global my_image
    filename = filedialog.askopenfilename(initialdir=".", title="Select a File", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("all files" , "*.*")))

    my_label = Label(root,text=filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(filename))
    my_image_label = Label(image=my_image).pack()


my_btn
 = Button(root, text="Open Image", command = open).pack()

root.mainloop()