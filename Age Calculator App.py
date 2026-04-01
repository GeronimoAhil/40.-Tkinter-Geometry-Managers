from tkinter import *
import math

root = Tk()
root.title("Age Calculator App")
root.geometry('400x400')

frame = Frame(master = root, height = 200, width = 360, bg = "#d0efff")

lbl1 = Label(frame, text = "Full name", bg = "#3895D3", fg = "white, width = 12")
lbl2 = Label(frame, text = "Your Age", bg = "#3895D3", fg = "white, width = 12")
name_entry = Entry(frame)
email_entry = Entry(frame)

def display():
    name = name_entry.get()
    greet = "Hey "+name
    message = "\nYou are ye"
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(g = "#BEBEBE", fg = "black")

btn = Button(text = "", command = display, bg = "red")

frame.place(x = 20, y = 0)
lbl1.place(x = 20, y = 20)
name_entry.place(x = 150, y = 20)
lbl2.place(x = 20, y = 80)
email_entry.place(x = 150, y = 80)
btn.place(x = 130, y = 210)
textbox.place(y = 250)

root.mainloop()