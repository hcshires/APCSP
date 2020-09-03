#####
# bouncing_ball.py
# 
# Creates a Scale and a Canvas. Animates a circle based on the Scale
# (c) 2013 PLTW
# version 11/1/2013
####

import tkinter as Tkinter #often people import Tkinter as *
import random

# Create root window 

root = Tkinter.Tk()
root.wm_title("Gentry's Ball Game")

#####
# Create Model
######

speed_intvar = Tkinter.IntVar()
speed_intvar.set(3) # Initialize y coordinate
# radius and x-coordinate of circle
r = 10
x = 150
y = 150
direction = 0.7 # radians of angle in standard position, ccw from positive x axis
fps = 10 # Amount of times animate() will be ran
go = True

colors = ["#ff0000", "#00ff00", "#0000ff", "#fff000"] # List of colors to change the ball color
 
######
# Create Controller
#######

# Instantiate and place slider
speed_slider = Tkinter.Scale(root, from_=5, to=1, variable=speed_intvar,    
                              label='speed')
speed_slider.grid(row=1, column=0, sticky=Tkinter.W)
# Create and place directions for the user
text = Tkinter.Label(root, text='Drag slider \nto adjust\nspeed.')
text.grid(row=0, column =0)

######
# Create View
#######

# Create and place a canvas
canvas = Tkinter.Canvas(root, width=600, height=600, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=1)
canvas.focus_set() # Give the focus of the program to the canvas, so it can handle key events

# Change the speed of the ball when keys pressed
def speedUp(event):
	s = speed_intvar.get()
	s += 1
	speed_intvar.set(s)
	
def speedDown(event):
	s = speed_intvar.get()
	s -= 1
	speed_intvar.set(s)

# Changes the state of the ball (animated or not animated)
def go_stop(event):
	global go # I wanna change the value of go
	# print(event.char) <- Character of key
	if event.char == " ": # Key code for space
		go = not go # Sets go to the opposite of the current value (toggles)

# Change the color of the ball randomly when a key is pressed
def color(event):
	i = random.randint(0, len(colors)-1) # Index used for the list of colors
	canvas.itemconfig(circle_item, fill=colors[i])

# Bind key events to canvas
canvas.bind("<Up>", speedUp)
canvas.bind("<Down>", speedDown)
canvas.bind("<Key>", go_stop)
canvas.bind("<c>", color)

# Create a circle on the canvas to match the initial model
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, 
                                 outline='#000000', fill='#00FFFF')
								 
import math

# Animates the ball
def animate():
    global direction
    # Get the slider data and create x- and y-components of velocity
    velocity_x = speed_intvar.get() * math.cos(direction) # adj = hyp*cos()
    velocity_y = speed_intvar.get() * math.sin(direction) # opp = hyp*sin()
    if go:
	    canvas.move(circle_item, velocity_x, velocity_y)
    # Change the canvas item's coordinates
    x1, y1, x2, y2 = canvas.coords(circle_item)
    # Get the new coordinates and act accordingly if ball is at an edge
    # If crossing left or right of canvas
    if x2 > canvas.winfo_width() and x1 > canvas.winfo_width(): # CHANGE TO WRAP THIS
        canvas.coords(circle_item, (r, y1+r, r+r, y1-r))
        # direction = math.pi - direction # Reverse the x-component of velocity
    # If crossing top or bottom of canvas
    if y2> canvas.winfo_height() or y1<0: 
        direction = -1 * direction # Reverse the y-component of velocity
    
    # Create an event in 1 msec that will be handled by animate(),
    # causing recursion        
    canvas.after(fps, animate)
# Call function directly to start the recursion
animate()

#######
# Event Loop
#######
root.mainloop()