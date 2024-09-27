# SpaceGame - Documentation

## Basics

### Create a Window

To create a simple window we will use tkinter. Using the following Code we can create a simple window:

```py
from tkinter import *
root = Tk()
root.mainloop()
```

![simple window](/assets/simple_window.png)  
with the following lines we can customize the window:

```py
root.title("Tk Example")
root.configure(background="yellow")
root.minsize(200, 200)  # width, height
root.maxsize(500, 500)
root.geometry("400x300+50+50")  # width x height + x + y
```

![custom_simple_window](/assets/custom_simple_window.png)  
title etits the window title. With configure we can change the background color. With minsize and maxsize we can define the minimal and maximal size of the window. With geometry we can change the initial windowsize.

### Create a Label

We can create a Label with the following code:

```py
from tkinter import *

root = Tk()
root.title("Tk Example")
root.minsize(200, 200)  # width, height
root.geometry("300x300+50+50")

# Create Label in our window
text = Label(root, text="Nothing will work unless you do.")
text.pack()
text2 = Label(root, text="- Maya Angelou")
text2.pack()
root.mainloop()
```

The first part is just creating a window, the second part is important for the label. We can no add text to our window.
![label_1](/assets/label_1.png)  
There are different ways to place the text by using `place()` or `grid()`.  
By using the following code we can add images to our window:

```py
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
```

![label_image.png](/assets/label_image.png)  

## Layout Design

### Frame Widget

To organize the different labels and images in our window we can use frames. Frames are like mini-windows or boxes within our main-window. To do so we can use the following code:

```py
from tkinter import *

root = Tk()  # create root window
root.title("Frame Example")
root.config(bg="skyblue")

# Create Frame widget
left_frame = Frame(root, width=200, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)
right_frame = Frame(root, width=400, height=400)
right_frame.grid(row=0, column=1, padx=10, pady=5)
root.mainloop()
```

First we give a name to our frame (here left_frame). Then we define the size of this frame, by using `Frame()`. Then we define the position of the frame by using `frame_name.grid()`. `row` tells us where the frame will be placed from the top and `column` tells us where from the left, starting with 0. `padx` and `pady` we define the space between the different frames.  
![frame_design](/assets/frame_design.png)  
By adding following lines we can add frames in frames to further divide the frames and add labels to specific frames:

```py
# Create frame within left_frame
tool_bar = Frame(left_frame, width=180, height=185, bg="purple")
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# Create label above the tool_bar
Label(left_frame, text="Example Text").grid(row=1, column=0, padx=5, pady=5)
```

We are adding the frame 'tool_bar' to the frame 'left_frame' by defining it in the first parameter of the `Frame()`-function. We can also tell a label to be in the 'left_frame' and then tell it where it should be on the grid, by using `.grid()`.
![frame_in_frame](/assets/frame_in_frame.png)  
