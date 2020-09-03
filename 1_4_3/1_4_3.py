'''
Change pixels in an image.
'''
import matplotlib.pyplot as plt
import os.path
import numpy as np  # "as" lets us use standard abbreviations
   
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)
img2 = plt.imread(filename)


# print(type(img))
# print(img[0])
height = len(img)
width = len(img[0])
# print(height, width)

img.setflags(write = 1)
img2.setflags(write = 1)

for row in range(420, 465): # height span of earing
    for column in range(120, 160): # width span of earing
        img[row][column] = [0, 255, 0] # green

for r in range(420, 467):
    for c in range(120, 162):
        if sum(img2[r][c])>400: # brightness R+G+B goes up to 3*255=765
            img2[r][c]=[255,0,255] # R + B = magenta
		
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img2, interpolation='none')

# Show the figure on the screen
plt.show()