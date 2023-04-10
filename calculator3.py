from tkinter import *
import tkinter as tk
import math

root = Tk()
root.title("Calculator-by anant")

logo_image = tk.PhotoImage(file="C:\\Users\\Anant\\Pictures\\calculator.png")
root.iconphoto(False, logo_image)

root.configure(bg='white smoke')

root.geometry("430x500")   
expression = ""

def setexpression(num):
    global expression
    expression = expression + str(num)
    value.set(expression)

def calculator():
    try:
        global expression
        answer = str(eval(expression))
        value.set(answer)
    except:
        value.set("ERROR! INVALID EXPRESSION")
        expression = ""

def clear():
    global expression
    expression = ""
    value.set(expression)

large_font = ('bold', 15)
small_font = ('bold', 10)

b = 1

value = StringVar(value="Enter expression")

Entry(root, textvariable=value, fg="white", bg="black", font=large_font).grid(row=0, column=0, columnspan=4, ipadx=70)

def create_circular_button(text, row, column, command):
    radius = 40
    x = (column * 90) + 20
    y = (row * 90) - 40
    button = Canvas(root, width=radius*2, height=radius*2, bd=0, highlightthickness=0,)
    button.create_oval(0, 0, radius*2, radius*2 ,fill="black")
    button.create_text(radius, radius, text=text,font=small_font, fill='white')
    button.place(x=x, y=y)
    button.bind("<Button-1>", lambda event: command())
    return button

create_circular_button("+", 2, 0, lambda: setexpression("+"))
create_circular_button("-", 3, 0, lambda: setexpression("-"))
create_circular_button("X", 4, 0, lambda: setexpression("*"))
create_circular_button("/", 5, 0, lambda: setexpression("/"))
create_circular_button("1", 2, 1, lambda: setexpression("1"))
create_circular_button("2", 2, 2, lambda: setexpression("2"))
create_circular_button("3", 2, 3, lambda: setexpression("3"))
create_circular_button("4", 3, 1, lambda: setexpression("4"))
create_circular_button("5", 3, 2, lambda: setexpression("5"))
create_circular_button("6", 3, 3, lambda: setexpression("6"))
create_circular_button("7", 4, 1, lambda: setexpression("7"))
create_circular_button("8", 4, 2, lambda: setexpression("8"))
create_circular_button("9", 4, 3, lambda: setexpression("9"))
create_circular_button("0", 5, 2, lambda: setexpression("0"))
create_circular_button(".", 5, 1, lambda: setexpression("."))
create_circular_button("a^2", 1, 1, lambda: setexpression("**2"))
create_circular_button("square root", 1, 2, lambda: setexpression("**.5"))
create_circular_button("=", 5, 3, calculator)
create_circular_button("Clear", 1, 0, clear)

root.mainloop()
