from tkinter import *

root = Tk()
'''
https://www.youtube.com/watch?v=YXPyB4XeYLA
'''

def myClick():
    myLabel = Label(root, text="Look, I clicked a button!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", state=NORMAL, command=myClick, fg= '#ffffaa', bg='green') # Don't type parentheses in the command buttons
myButton.pack()
root.mainloop()