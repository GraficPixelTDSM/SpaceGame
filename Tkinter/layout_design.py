from tkinter import *

root = Tk()  # create root window
root.title("Frame Example")
root.config(bg="skyblue")

# Create Frame widget
left_frame = Frame(root, width=200, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)
right_frame = Frame(root, width=400, height=400)
right_frame.grid(row=0, column=1, padx=10, pady=5)

# Create frame within left_frame
tool_bar = Frame(left_frame, width=180, height=185, bg="purple")
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# Create label above the tool_bar
Label(left_frame, text="Example Text").grid(row=1, column=0, padx=5, pady=5)

root.mainloop()
