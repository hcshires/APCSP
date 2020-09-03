import tkinter as tk
import random

times_clicked = 0
def clicked(event):
	global times_clicked #use the global variable within this function
	x = event.x # the x coordinate of your click
	y = event.y  # the y coordinate of your click
	rect_coords = canvas.coords(1) # get rectangle coordinates
	print(rect_coords) # print the coordinates of the rectangle when you click the screen (the rectangle has an ID of 1)
	if x >= rect_coords[0] and x <= rect_coords[2] and y >= rect_coords[1] and y <= rect_coords[3]:
		times_clicked = times_clicked + 1
		print("You've clicked the rectangle", times_clicked, "times!") # prints the value of times_clicked



def move_rect():
	width = window.winfo_width()
	height = window.winfo_height()
	new_x = random.randint(0, width)
	new_y = random.randint(0, height)
	
	canvas.coords(1, new_x, new_y, new_x + rect_w, new_y + rect_h)
	
	canvas.after(1000, move_rect)  # call the move function again after 1 second
	
	
window = tk.Tk( ) # create root window


window.geometry('350x200') # resize window

canvas = tk.Canvas(window, bg = "#efe745") #create canvas to draw on
canvas.pack(fill = tk.BOTH, expand = 1)  # make canvas fill window
rect_w = 100
rect_h = 50
rect = canvas.create_rectangle(50, 25, 50 + rect_w, 25 + rect_h, fill="blue")
window.bind("<Button-1>", clicked)  # set the event handler for when window is clicked 
move_rect()
window.mainloop()  # required line to start window 