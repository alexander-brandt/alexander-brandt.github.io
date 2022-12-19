import os
from PIL import Image

SCALE = 0.4

header = True
for line in open("Website_Names_Master.tsv"):
    if header:
        header = False
        continue
    tokens = line.split('\t')
    image = Image.open('./qr_codes_with_label/' + tokens[7] + '.png')
    x, y = image.size
    new_image = image.resize((int(x * SCALE), int(y * SCALE)))
    new_image.save('./qr_codes_with_label_resized/' + tokens[7] + '.png')