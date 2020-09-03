import matplotlib.pyplot as plt

# Read the image data into an array
img = plt.imread("woman.bmp")
img2 = plt.imread("woman9.bmp")

# Decoding string
alpha = "abcdefghijklmnopqrstuvwxyz 0123456789.,'?!-"
length = 0 # Length of string (init)

def readImage(original_img, encoded_img):
	'''Inputs two images, one with altered pixels from the original, 
	and outputs the first two pixel bit values to determine the length of the secret message
	'''

	# Read in the first two pixels to determine the length of the message
	pixel = original_img[0][0] - encoded_img[0][0]
	pixel2 = original_img[0][1] - encoded_img[0][1]
	
	# print(pixel)
	# print(pixel2)
	
	# Convert to binary for a six-bit string
	binary1 = format(pixel[0], '02b') + format(pixel[1], '02b') + format(pixel[2], '02b') 
	binary2 = binary1 + format(pixel2[0], '02b') + format(pixel2[1], '02b') + format(pixel2[2], '02b') # Add to make a 12-bit string
	# print(binary2)
	
	# Convert back to decimal to find the numerical length
	msgLen = int(binary2, base = 2) 
	# print(msgLen) # Uncomment for how many characters are in the string
	return msgLen
	
def decodeMsg(original_img, encoded_img, msgLen):
	'''Inputs the images and the length determined by readImage(),
	and outputs the decoded message from the altered image
	'''
	
	alphaIndex = 0 # index for alpha
	message = "" # init message
	
	for i in range(msgLen):
		
		# Finds the difference between two pixels to find how much they changed (i+2 to exclude the first two pixels, as they were for determining msg length)
		pixels = original_img[0][i+2] - encoded_img[0][i+2]
		msgBinary = format(pixels[0], '02b') + format(pixels[1], '02b') + format(pixels[2], '02b') # Adds each pixel 2-bit to a 6-bit character string for a character index
		alphaIndex = int(msgBinary, base = 2) # convert to decimal for an index value
		message += alpha[alphaIndex] # Add a character to message from alpha using the index found by the numerical value from the binary
		
	return message

length = readImage(img, img2) # Set length to value returned by readImage
print(decodeMsg(img, img2, length)) # Print the message!