from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Title of this software")
root.iconbitmap('favicon.ico')


# Types of messages: showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup(type):
    
    if type == 'info':
        response = messagebox.showinfo("This is my Popup!", "Hello World!")
    elif type == 'warning':
        response = messagebox.showwarning("This is my Warning!", "Hello World!")
    elif type == 'error':
        response = messagebox.showerror("This is my Error!", "Hello World!")
    elif type == 'askquestion':
        response = messagebox.askquestion("This is my Question!", "Hello World!")
    elif type == 'askokcancel':
        response = messagebox.askokcancel("This is my OK CANCEL BOX!", "Hello World!")
    elif type == 'askyesno':
        response = messagebox.askyesno("This is my OK CANCEL BOX!", "Hello World!")
    else:
        response = messagebox.showinfo("This is my Popup!", f"Unrecognised type {type}!")
    Label(root, text=response).pack()

Button(root, text="Info", command=lambda:popup('info')).pack()
Button(root, text="Warning", command=lambda:popup('warning')).pack()
Button(root, text="Error", command=lambda:popup('error')).pack()
Button(root, text="Ask Question", command=lambda:popup('askquestion')).pack()
Button(root, text="Ask OK Cancel", command=lambda:popup('askokcancel')).pack()
Button(root, text="Ask Yes No", command=lambda:popup('askyesno')).pack()
Button(root, text="Something Else", command=lambda:popup('somethingelse')).pack()



root.mainloop()