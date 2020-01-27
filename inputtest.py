from tkinter import *

root = Tk()
'''
https://www.youtube.com/watch?v=YXPyB4XeYLA
'''
e = Entry(root, width=50, bg="blue", fg="white", borderwidth=0.5)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", state=NORMAL, command=myClick, fg= '#ffffaa', bg='green') # Don't type parentheses in the command buttons
myButton.pack()
root.mainloop()