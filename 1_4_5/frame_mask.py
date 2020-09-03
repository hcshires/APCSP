import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            

def frame_image(original_image, bw = 10, color = (255, 0, 0, 255)): # bw = border width
    ''' Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner radius as a portion of the shorter dimension of original_image
    '''
    #set the radius of the rounded corners
    width, height = original_image.size
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0)) # 0 in alpha is transparent
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask) # make a layer to draw on
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    drawing_layer.polygon([(bw, bw), (width - bw, bw), 
						(width - bw, height - bw), (bw, height - bw)], fill = color) # color does not matter, as long as the value is opaque
    # Uncomment the following line to show the mask
    # plt.imshow(rounded_mask)
    
    # Make the new image, instead of pasting onto a transparent background, paste onto background of specified color
    result = PIL.Image.new('RGBA', original_image.size, color) # new background to paste the image on
    result.paste(original_image, (0,0), mask=rounded_mask) # uses mask. defines the stuff that actually shows up. a "filter" for the original image
    return result
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregators
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def frame_all_images(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with default percent of radius
        curr_image = image_list[n]
        new_image = frame_image(curr_image, bw = 20, color = (0, 102, 255)) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
		
frame_all_images()