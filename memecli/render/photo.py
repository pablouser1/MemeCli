from PIL import Image, ImageDraw, ImageFont
from memecli.helpers.Config import getConfig

class PhotoRender:
    config = {}
    image: Image.Image
    draw: ImageDraw

    def __init__(self, template: str, config: dict):
        self.config = config
        self.image = Image.open(template)
        self.draw = ImageDraw.Draw(self.image)

    def get_font_size(self, text, font, max_width=None, max_height=None):
        if max_width is None and max_height is None:
            raise ValueError('You need to pass max_width or max_height')
        font_size = 1
        text_size = self.get_text_size(font, font_size, text)
        if (max_width is not None and text_size[0] > max_width) or \
           (max_height is not None and text_size[1] > max_height):
            raise ValueError("Text can't be filled in only (%dpx, %dpx)" % \
                    text_size)
        while True:
            if (max_width is not None and text_size[0] >= max_width) or \
               (max_height is not None and text_size[1] >= max_height):
                return font_size - 1
            font_size += 1
            text_size = self.get_text_size(font, font_size, text)

    def write_text(self, xy, text, font_filename,
                   color=(0, 0, 0), max_width=None, max_height=None):
        x, y = xy
        font_size = self.get_font_size(text, font_filename, max_width, max_height)
        text_size = self.get_text_size(font_filename, font_size, text)
        font = ImageFont.truetype(font_filename, font_size)
        self.draw.text((x, y), text, font=font, fill=color)
        return text_size

    def get_text_size(self, font_filename, font_size, text):
        font = ImageFont.truetype(font_filename, font_size)
        return font.getsize(text)

    def run(self, texts: list):
        # Texts
        if 'texts' in self.config:
            for i in range(len(self.config["texts"])):
                text_config = self.config["texts"][i]
                self.write_text(tuple(text_config["pos"]), texts[i], font_filename="/usr/share/fonts/TTF/DejaVuSerif.ttf", max_width=text_config["size"][0], max_height=text_config["size"][1])

    def save(self, file: str):
        self.image.save(file)

    def cleanup(self):
        pass
