from PIL import Image, ImageDraw, ImageFont 
from random import sample, choice, randrange


class Captcha:
    def __init__(self, captcha_size):
        self.captcha_size = captcha_size

    def create_captcha(self, font_size, count):
        self.img = Image.new("RGB", self.captcha_size, "#ffffff")
        font = ImageFont.truetype('arial.ttf', size=font_size)
        draw_text = ImageDraw.Draw(self.img)
        generation_text = self.generateSymb(count)
        w, h = font.getsize(generation_text)
        draw_text.text(
            ((self.captcha_size[0] - w) / 2, (self.captcha_size[1] - h) / 2),
            generation_text,
            font=font,
            fill=(0, 0, 0))
        self.img.show()
        return generation_text
    
    def generateSymb(self, count):
        letters = "qwertyuiopzxcvbnm1234567890"
        random = [choice(letters.upper()) if randrange(0, 2) > 0 else choice(letters.lower()) for i in range(count * 3)]
        return ''.join(sample(random, k=count))


Captcha([200, 100]).create_captcha(font_size=32, count=5)