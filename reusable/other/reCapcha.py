
from captcha.image import ImageCaptcha
import random

def capcha():
    img = ImageCaptcha()
    image = img.generate_image(str(random.randint(10000, 100000)))
    image.save("random.jpeg")

capcha()