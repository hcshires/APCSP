""" TkinterDraw.py demonstrates some methods of Tkinter.Canvas
Revision 10/29/2013 Copyright 2013 PLTW
"""
# When you import with *, you DON'T have to reference the librart name when calling function.
from tkinter import * 			# Use sparlingly, so you understand where functions come from
import PIL.Image, PIL.ImageTk
import os.path         
root = Tk()						# create main window

# Make and place a canvas widget for events and drawing
canvas = Canvas(root, height=600, width=500, relief=RAISED, bg='white')
canvas.grid() # Puts the canvas in the main Tk window

# Make four objects on the canvas
checkbox = canvas.create_rectangle(100, 200, 200, 300, dash=[1,4]) # top-left, bottom-right coordinates
check = canvas.create_line(100, 250, 150, 300, 220, 150, fill='red', width=20)
message = canvas.create_text(380, 250, text='Try this!', font=('Arial', -100))
shadow = canvas.create_oval(100, 450, 500, 550, fill='#888888', outline='#888888')

# Useful values to understand
print(checkbox, check, message, shadow)
print("the coordinates of item 1 on the canvas are", canvas.coords(checkbox))

# Make an array of objects on the canvas
circles=[]

for r in range(10, 60, 10):
	circles += [canvas.create_oval(300-r, 400-r, 300+r, 400+r, outline='red')]

canvas.itemconfig(circles[0], fill='black') # Change color
canvas.itemconfig(circles[0], width=2) # Increase width
canvas.itemconfig(circles[2], outline='black')

a, b, c, d = canvas.coords(circles[0]) # Get coordinates
e, f, g, h = canvas.coords(circles[2])

canvas.coords(circles[0], a+5, b, c+5, d) # Change coordinates
canvas.coords(circles[2], e, f-5, g, h-5)
	
# Make one more object on the canvas
canopy = canvas.create_arc(0, 50, 800, 850, start=30, extent=100, width=10, style=ARC)
# canopy = canvas.create_arc(0, 50, 600, 650, start=30, extent=120, width=50, style=ARC)
							
# Get a filename in the same directory as this program
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'canopyIcon.jpg')
  
# Open the image file and convert to an ImageTk object
img = PIL.Image.open(filename) # create a PIL.Image from the jpg file
tkimg = PIL.ImageTk.PhotoImage(img) # convert the PIL.Image to a PIL.TkImage
  
# Add the ImageTk object to the canvas.
icon = canvas.create_image(150, 250, image=tkimg) # Causes the error when not fixed

# Enter event loop. This displays the GUI and starts listening for events.
# The program ends when you close the window.
root.mainloop()