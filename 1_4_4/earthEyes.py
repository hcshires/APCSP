'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

import PIL
import matplotlib.pyplot as plt
import os.path

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))
student_file = os.path.join(directory, 'student.jpg')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)
plt.show()

# Open, resize, and display earth
earth_file = os.path.join(directory, 'earth.png')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
plt.show()

# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(earth_small, (1162, 966), mask=earth_small)
student_img.paste(earth_small, (710, 948), mask=earth_small)
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
plt.show()

# bytes/pixel
''' each pixel has RGBA bands, each band can range from 0 to 255, which requires 8 bits  i.e. 1 BYTE
so RGBA takes 4 BYTES of information.
227,525 px <- earth_img
4 bytes/px = 910,100 bytes or 910.1 KB
'''
print(student_img.size)
print(earth_img)
print(earth_small.size)
print(earth_img.size[1])
