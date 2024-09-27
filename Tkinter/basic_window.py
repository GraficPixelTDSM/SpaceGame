from tkinter import *

root = Tk()  # create a root widget
root.title("Tk Example")
root.configure(background="yellow")
root.minsize(200, 200)  # width, height
root.maxsize(500, 500)
root.geometry("400x300+50+50")  # width x height + x + y
root.mainloop()
