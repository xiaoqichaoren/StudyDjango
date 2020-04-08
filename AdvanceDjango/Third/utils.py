import random
from io import BytesIO

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw

from AdvanceDjango import settings


class DrawVerify:
    def __init__(self, size=(200, 100), mode='RGB', font_path=settings.FONT_PATH):
        self.size = size
        mode = mode
        bg_color = self.RGB()
        self.image = Image.new(mode=mode, size=self.size, color=bg_color)
        self.draw = ImageDraw(self.image, mode)
        self.font = ImageFont.truetype(font_path, 20)
        self.code_length = 4
        self.code = self.CAPTCHA()

    def RGB(self):
        r = random.randrange(256)
        g = random.randrange(256)
        b = random.randrange(256)
        return r, g, b

    def CAPTCHA(self):
        # 生成随机数字
        code = ''
        for i in range(self.code_length):
            code += str(random.randrange(10))
        return code

    def draw_CAPTCHA(self):
        # 图片的随机位置
        xy = [random.randrange(50, self.size[0] - 50), random.randrange(25, self.size[1] - 25)]
        # 画
        for i in range(len(self.code)):
            fill = (self.RGB())
            xy[0] = xy[0] + 10
            self.draw.text(xy=xy, text=self.code[i], imagefont=self.font, fill=fill)

    def draw_point(self):
        # 干扰图形
        for i in range(100):
            fill = (self.RGB())
            xy = (random.randrange(self.size[0]), random.randrange(self.size[1]))
            self.draw.point(xy=xy, fill=fill)

    def Do(self):
        """
        绘制一张验证码图片
        :return: 验证码
        """
        self.draw_CAPTCHA()
        self.draw_point()
        return self.code
