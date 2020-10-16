from PIL import Image, ImageDraw, ImageFont 
from random import sample, choice, randrange, randint


class Captcha:
    def __init__(self, captcha_size):
        self.captcha_size = captcha_size

    def create_captcha(self, font_size, count):
        self.img = Image.new("RGB", self.captcha_size, "#ffffff")
        pix = self.img.load()
        font = ImageFont.truetype('arial.ttf', size=font_size)
        draw = ImageDraw.Draw(self.img)
        generation_text = self.generateSymb(count)
        w, h = font.getsize(generation_text)
        draw.text(
            ((self.captcha_size[0] - w) / 2, (self.captcha_size[1] - h) / 2),
            generation_text,
            font=font,
            fill=(0, 0, 0))
        for i in range(count * 3):
            draw.line(
                (randrange(0, self.captcha_size[0]), randrange(0, self.captcha_size[1]), 
                randrange(0, self.captcha_size[0]), randrange(0, self.captcha_size[1])),
                fill=(0, 0, 0), width=3)
        for x in range(self.captcha_size[0]):
            for y in range(self.captcha_size[1]):
                rand = randint(-70, 70)
                a = pix[x, y][0] + rand
                b = pix[x, y][1] + rand
                c = pix[x, y][2] + rand
                draw.point((x, y), (0 if a < 0 or b < 0 or c < 0 else 255, 0 if b < 0 else 255, 0 if c < 0 else 255))
        self.img.save("captcha_test.png")
        return generation_text
    
    def generateSymb(self, count):
        letters = "qwertyuiopzxcvbnm1234567890"
        random = [choice(letters.upper()) if randrange(0, 2) > 0 else choice(letters.lower()) for i in range(count * 3)]
        return ''.join(sample(random, k=count))


Captcha([220, 100]).create_captcha(font_size=70, count=5)
