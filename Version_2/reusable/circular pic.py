
from PIL import Image, ImageOps, ImageDraw
import os

size = (500, 500)
mask = Image.new('L', size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + size, fill=255)

im = Image.open(os.path.abspath(os.getcwd()+'/pychat.png'))

output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
output.putalpha(mask)

output.save('output.png')
