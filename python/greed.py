from tkinter import *

root = Tk()

label1 = Label(root, text="Имя")
label2 = Label(root, text="Парооль")


entry_1 = Entry(root)
entry_2 = Entry(root)

label1.grid(row=0, column=0, stick=E)  #приклеиться к востоку ячейки
label2.grid(row=1, column=0)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Остаться в системе")
c.grid(columnspan=2)  # 2 колонки


root.mainloop()