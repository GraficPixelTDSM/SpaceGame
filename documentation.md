# SpaceGame - Documentation
## Basics
### Create a Window
To create a simple window we will use tkinter. Using the following Code we can create a simple window:
```
from tkinter import *
root = Tk()
root.mainloop()
```
![simple window](/assets/simple_window.png)  
with the following lines we can customize the window:
```
root.title("Tk Example")
root.configure(background="yellow")
root.minsize(200, 200)  # width, height
root.maxsize(500, 500)
root.geometry("400x300+50+50")  # width x height + x + y
```
![custom_simple_window](/assets/custom_simple_window.png)    
title etits the window title. With configure we can change the background color. With minsize and maxsize we can define the minimal and maximal size of the window. With geometry we can change the initial windowsize.