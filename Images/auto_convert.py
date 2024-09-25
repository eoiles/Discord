'''
This python script will detect all the jfif files in the current directory 
and convert them to png, saving them in a new 'png' folder.
'''

import os
import sys
from PIL import Image

# Get the directory where this script is located
dir_path = os.path.dirname(os.path.realpath(__file__))

# Create a 'png' folder inside the script's directory if it doesn't exist
output_dir = os.path.join(dir_path, 'png')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("Converting JFIF to PNG in dir: {}".format(dir_path))

# List all files in the script's directory
files = os.listdir(dir_path)

for file in files:
    # Check if the file is a .jfif file
    if file.endswith('.jfif'):
        dest_name = file.rsplit('.', 1)[0] + '.png'  # Change file extension to .png
        print("Converting: {} => {}".format(file, dest_name))
        img = Image.open(os.path.join(dir_path, file))
        # Convert and save the file in the 'png' folder
        img.save(os.path.join(output_dir, dest_name), 'PNG')

print("Conversion complete. All PNG files saved in 'png' folder.")