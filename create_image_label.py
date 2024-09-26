from tkinter import *

root = Tk()
root.title("Tk Example")
root.minsize(200, 200)  # width, height
root.geometry("450x350+50+50")

# Create Label in our window
text = Label(root, text="Nothing will work unless you do.")
text.pack()
text2 = Label(root, text="- Maya Angelou")
text2.pack()

image = PhotoImage(file="meme_1.png")
img = Label(root, image=image)
img.pack()
root.mainloop()
