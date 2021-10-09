from PIL import Image
import os

angle = 270 #90 degrees clockwise
size = (128,128)
original_path  = os.path.expanduser('~')
new_path = '/opt/icons/' #intended path

for media in os.listdir(original_path):
    if media == ".DS_Store":
        continue
    im = Image.open(original_path + media)
    im.rotate(angle).resize(size).convert("RGB").save(new_path + media + ".jpeg")
    im.close()
