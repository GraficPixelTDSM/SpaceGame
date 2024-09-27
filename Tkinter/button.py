from tkinter import *

root = Tk()  # create parent window

# use Button and Label widgets to create a simple TV remote
turn_on = Button(root, text="ON")
turn_on.pack()

turn_off = Button(root, text="OFF", command=root.quit)
turn_off.pack()

volume = Label(root, text="VOLUME")
volume.pack()

vol_up = Button(root, text="+")
vol_up.pack()

vol_down = Button(root, text="-")
vol_down.pack()

root.mainloop()
