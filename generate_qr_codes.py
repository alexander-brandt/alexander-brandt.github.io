import os
import sys

import pyqrcode
import png
from pyqrcode import QRCode
header = True
from PIL import ImageFont, ImageDraw, Image

# font = ImageFont.truetype("arial.ttf")
font = ImageFont.truetype("arial.ttf", 10)

for line in open("Website_Names_Master.tsv"):
    if header:
        header = False
        continue

    tokens = line.split("\t")
    print(tokens)
    url = pyqrcode.create("https://abrandtnewyear.com/pages/" + tokens[7] + ".html")
    url.png("./qr_codes/" + tokens[7] + ".png", scale=3)

    background = Image.new('RGBA', (134, 138), (255, 255, 255, 255))
    from PIL import ImageDraw
    draw = ImageDraw.Draw(background)
    qr = Image.open('./qr_codes/' + tokens[7] + '.png')
    background.paste(qr, (0, 0))
    x = draw.textlength(tokens[1], font=font)
    draw.text(((134 - x) / 2, 125), tokens[1], fill=(0, 0, 0), font=font)

    background.save('./qr_codes_with_label/' + tokens[7] + '.png')



