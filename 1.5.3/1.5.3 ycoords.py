#####
# radius_changer.py
# 
# Creates a Scale and a Canvas. Updates a circle based on the Scale.
# (c) 2013 PLTW
# version 11/1/2013
####

import tkinter as Tkinter #often people import Tkinter as * (Fix PLTW's dumb syntax)

#####
# Create root window 
####
root = Tkinter.Tk()

#####
# Create Model
######
y_intvar = Tkinter.IntVar()
radius_intvar = Tkinter.IntVar()
y_intvar.set(0) #initialize radius
# center of circle
radius_intvar.set(100)
x = 150
y = 150

######
# Create Controller
#######
# Event handler for slider
def y_changed(new_intval):
    # Get data from model
    # Could do this: r = int(new_intval)
    y_coords = y_intvar.get()
    # Controller updating the view
    canvas.coords(circle_item, x-r, y_coords-r, x+r, y_coords+r)
# Instantiate and place slider
radius_slider = Tkinter.Scale(root, from_=1, to=150, variable=y_intvar,    
                              label='Y Coordinate', command=y_changed)
radius_slider.grid(row=1, column=0, sticky=Tkinter.W)
# Create and place directions for the user
text = Tkinter.Label(root, text='Drag slider \nto adjust\ncircle.')
text.grid(row=0, column=0)

######
# Create View
#######
# Create and place a canvas
canvas = Tkinter.Canvas(root, width=300, height=300, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=1)

# Create a circle on the canvas to match the initial model
r = radius_intvar.get()
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, 
                                 outline='#000000', fill='#00FFFF')
#######
# Event Loop
#######
root.mainloop()