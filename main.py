from tkinter import *

root = Tk()

e = Entry(root)
e.grid(row = 0, column = 0)
e.insert(0, "Enter your name:")
def onClick():
    ans = e.get()
    output= Label(root, text = ans)
    output.grid(row = 1, column = 1)

but = Button(root, text = "Click!", commmand = onClick())
but.grid(row = 2, column = 0)

root.mainloop()
