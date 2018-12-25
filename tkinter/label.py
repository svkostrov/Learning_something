from tkinter import *

root = Tk()

one = Label(root, text="РАЗ!", bg="red", fg="yellow")
one.pack()

two = Label(root, text="ДВА!", bg="blue", fg="white")
two.pack(fill=X)

three = Label(root, text="ТРИ!", bg="green", fg="purple")
three.pack(side=LEFT, fill=Y)


root.mainloop()