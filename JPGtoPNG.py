# Run the script python JPGtoPNG.py Pokedex/ new/
# convert images to png
from PIL import Image
import sys
import os

# grab first and second arguments
img_path, new_img_path = [sys.argv[1], sys.argv[2]]

# check if new/ exists, if not create
if not os.path.exists(new_img_path):
    os.makedirs(new_img_path)
    print("The new directory is created!")

# loop through Pokedex
# directory = os.fsencode(img_path)

for file in os.listdir(img_path):
    if file.endswith(".jpg"):
        img = Image.open(f"./{img_path}{file}")
        name_img = os.path.splitext(file)[0]
        img.save(f'./{new_img_path}{name_img}.png', 'png')
    else:
        continue
print("Done!")
