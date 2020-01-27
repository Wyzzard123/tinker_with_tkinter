from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Title of this software")
root.iconbitmap('favicon.ico')

def image(fp):
    return ImageTk.PhotoImage(Image.open(fp))

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])

    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda:back(image_number - 1))
    
    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=1, column=0, columnspan=4)
    button_back.grid(row=0, column = 0)
    button_forward.grid(row=0, column=2)
    
    status = Label(root, text=f"Image {image_number} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)

    status.grid(row=0, column=3, sticky=W+E)
    return

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])

    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda:back(image_number - 1))
    
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)


    status = Label(root, text=f"Image {image_number} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
    
    status.grid(row=0, column=3, sticky=W+E)

    my_label.grid(row=1, column=0, columnspan=4)
    button_back.grid(row=0, column = 0)
    button_forward.grid(row=0, column=2)

my_img1 = image("miku.png")
my_img2 = image("billy1.png")
my_img3 = image("billy2.png")
my_img4 = image("giorno.jpg")
my_img5 = image("part5.jpg")

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text=f"Image 1 of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=1, column=0, columnspan=4)


button_back = Button(root, text="<<", command=lambda:back(1), state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda:forward(2))

button_back.grid(row=0, column = 0)
button_exit.grid(row=0, column=1)
button_forward.grid(row=0, column=2, pady = 10)
status.grid(row=0, column=3, sticky=W+E)


root.mainloop()