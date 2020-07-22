
from PIL import Image, ImageOps, ImageDraw
import os

#circle pic
size = (500, 500)
mask = Image.new('L', size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + size, fill=255)
from PIL import ImageFilter
im = Image.open(os.path.abspath(os.getcwd()+'/output.png'))
output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
output.putalpha(mask)
output.save('output2.png')

#blur pic
from PIL import ImageFilter

blurred_image = im.filter(ImageFilter.BLUR)
blurred_image.save('output3.png')