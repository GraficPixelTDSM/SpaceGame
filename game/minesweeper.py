from tkinter import *
from random import *

root = Tk()
variabeln = {}
values = {}


def create_vars():
    for i in range(10):
        for j in range(10):
            variabeln[f"var_{i}{j}"] = values[i][j]

    print(variabeln)


def create_root_window():
    root.title("Minesweeper")
    root.maxsize(900, 600)
    root.config(bg="skyblue")
    txt = Label(root, text="test")
    txt.pack()
    root.mainloop()


def create_values():
    values = [[randint(0, 10) for i in range(10)] for j in range(10)]
    print(values)
    return values


def button_pressed(x, y):
    print(f"button {x}, {y} has been pressed")


create_root_window()
values = create_values()
create_vars()
