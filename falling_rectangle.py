import tkinter as tk
import random

xvel = 0
times_clicked = 0
yvel = -5
def clicked(event):
	global times_clicked #use the global variable within this function
	x = event.x # the x coordinate of your click
	y = event.y  # the y coordinate of your click
	print(canvas.coords(1)) # print the coordinates of the rectangle when you click the screen (the rectangle has an ID of 1)

def move_rect():
	global yvel
	global xvel
	width = window.winfo_width()
	height = window.winfo_height()
	pos = canvas.coords(1) # get current rectangle coordinates
	new_y = pos[1]+yvel
	new_x = pos[0]+xvel
	if new_y <= height:
		canvas.coords(1, new_x, new_y,  new_x + rect_w, new_y + rect_h)
	yvel += .25
	
	canvas.after(100, move_rect)  # call the move function again after .5 second

def up(event):
	global yvel
	yvel = yvel - 2

def left(event):
	global xvel 
	xvel = xvel - 2

def right(event):
	global xvel 
	xvel = xvel + 2 
	
def collisionDetection():
	
	
	
	
window = tk.Tk( ) # create root window 


window.geometry('700x400') # resize window

canvas = tk.Canvas(window, bg = "#ffffff") #create canvas to draw on
canvas.pack(fill = tk.BOTH, expand = 1)  # make canvas fill window
rect_w = 100
rect_h = 50
player = canvas.create_rectangle(200, 100, 200 + rect_w, 100 + rect_h, fill="blue") # draws rectangle
landingRect = canvas.create_rectangle(0, 300, 700, 400, fill="black")
window.bind("<Button-1>", clicked)  # set the event handler for when window is clicked 
window.bind("<w>", up)
window.bind("<a>", left)
window.bind("<d>", right)
move_rect()
window.mainloop()  # required line to start window 