from PIL import Image
import os

# Run this in the same folder as the buttons. This script WILL overwrite all buttons.
# This script will only run if a corresponding "border.png" is included in the folder
# This script assumes that the buttons are the same size as both "border.png" and "gradient.png"

cwd = os.getcwd()
file_exists = os.path.exists('gradient.png')
for filename in os.listdir(cwd):
    if filename.endswith(".png"):
        if filename != "border.png" and filename != "gradient.png":
            # Opens the Files
            background = Image.open(filename).convert("RGBA")
            foreground = Image.open("border.png").convert("RGBA")
            # Merge the Images
            x, y = background.size
            background.paste(foreground, (0, 0, x, y), foreground)
            
            # Save the Images
            size = len(filename)
            Image.alpha_composite(background, foreground).save(filename)
            if file_exists:
                # Opens the Files
                background = Image.open("gradient.png").convert("RGBA")
                foreground = Image.open(filename).convert("RGBA")
                # Merge the Images
                x, y = background.size
                background.paste(foreground, (0, 0, x, y), foreground)
                
                # Save the Images
                size = len(filename)
                Image.alpha_composite(background, foreground).save(filename)