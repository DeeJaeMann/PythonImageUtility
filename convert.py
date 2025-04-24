from PIL import Image
from collections import Counter
import os

root_dir = "/home/deemann/local/src/PythonImageUtility/"

for filename in os.listdir(root_dir + "images"):
    print(f'Begin Loop: {filename}')
    file_path = os.path.join(root_dir + "images", filename)
    print(f'File Path: {file_path}')
    if os.path.isfile(file_path):
        if ".DS_Store" in filename:
            pass
        else:
            print(f'File: {filename}')
            
            # Open and convert image to RGBA
            img = Image.open(file_path).convert('RGBA')

            # Get all pixels
            pixels = list(img.getdata())

            # Filter out transparent pixels
            opaque_pixels = [pixel for pixel in pixels if pixel[3] != 0]

            # Count each color
            color_counts = Counter(opaque_pixels)

            # Get the most common color
            foreground_color = color_counts.most_common(1)[0][0]

            # Check if the foreground color is black or white and assign opposite as background color
            if 0 in foreground_color:
                # Black foreground, background white
                bg_color = (255, 255, 255)
            else:
                # White foreground, background black
                bg_color = (0, 0, 0)

            # Create a new background image 
            background = Image.new('RGBA', img.size, bg_color)

            # Replace the transparent layer with the new background image
            alpha_composite = Image.alpha_composite(background, img)

            # Convert the image to RGB and format
            new_img = alpha_composite.convert("RGB")
            new_img = new_img.rotate(270).resize((128,128))

            # Save image as JPEG
            new_img.save(root_dir + "tmp/" + filename, "JPEG")

            img2 = Image.open(root_dir + "tmp/" + filename)
            print(img2.format, img2.size)

            #img2.show()