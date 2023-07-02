from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from . import tupleFunctions as tf
import random
from urllib.request import urlopen
from django.conf import settings
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

# from django.contrib.staticfiles.storage import staticfiles_storage


def make(img_author, img_title, img_slug):
    bg = background()
    name = img_author
    cover = author(bg, name)
    titles = title(cover, img_title)
    cover_image = save(titles, img_slug)
    name = img_slug + ".png"
    # file = open(cover_image, "rb")
    file = default_storage.open(cover_image, "rb")
    return file


def background():
    bg = "https://takadahmedia.s3.amazonaws.com/static/img/book_cover.png"
    im = Image.open(urlopen(bg))
    # blur the background
    enhancer = ImageEnhance.Sharpness(im)
    factor = 0.05
    im = enhancer.enhance(factor)
    # brighten the colour
    enhancer = ImageEnhance.Brightness(im)
    factor = 1.0
    im = enhancer.enhance(factor)
    return im


def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getbbox(text)[2] <= max_width - 10:
        lines.append(text)
    else:
        # split the line by spaces to get words
        words = text.split(" ")
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ""
            while i < len(words) and font.getbbox(line + words[i])[2] <= max_width:
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word,
            # add the line to the lines array
            lines.append(line)
    return lines


def author(image, name):
    # image = Image.open(image)
    draw = ImageDraw.Draw(image)
    truetype_url = "https://github.com/googlefonts/josefinsans/blob/master/fonts/ttf/JosefinSans-Bold.ttf?raw=true"
    # font = ImageFont.truetype(urlopen(truetype_url), size=15)
    font = ImageFont.truetype(urlopen(truetype_url), size=0)
    while font.getbbox(name)[2] < (image.size[0] - 40):
        font = ImageFont.truetype(urlopen(truetype_url), size=font.size + 1)
    (x, y) = (186, 490)
    color = "rgb(31, 69,60)"  # color
    border = "white"
    image_size = image.size
    lines = text_wrap(name, font, image_size[0] - 40)
    line_height = font.getbbox("hg")[3] - font.getbbox("hg")[1]

    for line in lines:
        # draw the line on the image
        draw.text(
            (x, y),
            line,
            fill=color,
            stroke_width=2,
            stroke_fill=border,
            font=font,
            anchor="ms",
        )
        y = y + line_height
    return image


def title(image, title):
    # image = Image.open(image)
    draw = ImageDraw.Draw(image)
    # create the ImageFont instance
    truetype_url = (
        "https://github.com/googlefonts/Fira/blob/main/ttf/FiraSans-Bold.ttf?raw=true"
    )
    font = ImageFont.truetype(urlopen(truetype_url), size=0)
    # Automatically get the font size
    while font.getbbox(title)[2] < image.size[0] + 20:
        font = ImageFont.truetype(urlopen(truetype_url), size=font.size + 1)
    color = "rgb(255, 255, 255)"  # white color
    border = "black"
    image_size = image.size
    lines = text_wrap(title, font, image_size[0] - 10)
    line_height = font.getbbox("hg")[3] - font.getbbox("hg")[1]

    x = 186
    y = 112
    # todo: Increase the font size each line of the text
    # this is supposed to increase the font size but whill check it later
    # while font.getbbox(lines[0])[2] < image_size[0] - 40:
    #     width = ImageFont.truetype(urlopen(truetype_url), size=font.size + 1)
    for line in lines:
        # while font.getbbox(line)[2] < image.size[0] + 20:
        #     font = ImageFont.truetype(urlopen(truetype_url), size=font.size + 1)
        # draw the line on the image
        draw.text(
            (x, y),
            line,
            fill=color,
            stroke_width=2,
            stroke_fill=border,
            font=width,
            anchor="ms",
        )

        # update the y position so that we can use it for next line
        y = y + line_height
    return image


def save(image, title):
    path = title + ".png"
    # image.save(path, "PNG")
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    # write straight to the system path
    f = default_storage.open(path, "wb")
    f.write(buffer.getvalue())
    f.close()

    return path
