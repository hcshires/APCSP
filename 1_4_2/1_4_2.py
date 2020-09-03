'''
Read and show an image.
'''
import matplotlib.pyplot as plt
import os.path
import numpy as np # “as” lets us use standard abbreviations
   
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)
print("Location:", filename)
  
'''Show the image data'''
# Create figure with n subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in a subplot
ax[0].bar(0, height=3, width=0.4, bottom=None, align='center', data=None, color='red') # creates a bar graph in 1 subplot
ax[1].imshow(img, interpolation='none') # shows an image in the other
ax[1].plot(43.9355, 35.027, 'ro')
ax[1].plot(67.9536, 26.5996, 'ro')
# Show the figure on the screen
plt.show()
'''
7a.) (291.5, 400.539)
'''

