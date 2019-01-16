from tkinter import *

root = Tk()

top_frame = Frame(root)
top_frame.pack(side=TOP)

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

button1 = Button(top_frame, text="Кнопка 1", fg="red")
button2 = Button(top_frame, text="Кнопка 2", fg="blue")
button3 = Button(top_frame, text="Кнопка 3", fg="green")
button4 = Button(bottom_frame, text="Кнопка 4", fg="gray")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


root.mainloop() # зациклим

