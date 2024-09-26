from tkinter import *

root = Tk()
root.title("Tk Example")
root.minsize(200, 200)  # width, height
root.geometry("450x350+50+50")

# Create Label in our window
image = PhotoImage(file="meme_1.png")
img = Label(root, image=image)
img.pack()
root.mainloop()
