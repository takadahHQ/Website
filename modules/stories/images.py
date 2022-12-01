from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from django.core.files import File

from . import tupleFunctions as tf
import glob, os, math
import random
from urllib.request import urlopen
from django.conf import settings


def make(img_author, img_title, img_slug):
    bg = background()
    name = img_author
    cover = author(bg, name)
    titles = title(cover, img_title)
    cover_image = save(titles, img_slug)
    name = img_slug + ".png"
    file = open(cover_image, "rb")
    return file


def background():
    startColor = (
        random.randrange(1, 66),
        random.randrange(1, 138),
        random.randrange(1, 255),
    )
    endColorX = (
        random.randrange(1, 65),
        random.randrange(1, 255),
        random.randrange(1, 255),
    )
    endColorY = (
        random.randrange(1, 118),
        random.randrange(1, 65),
        random.randrange(1, 255),
    )
    size = (300, 500)

    im = Image.new("RGB", size, "black")
    pixels = im.load()

    deltaX = (
        (endColorX[0] - startColor[0]) / float(size[0]),
        (endColorX[1] - startColor[1]) / float(size[0]),
        (endColorX[2] - startColor[2]) / float(size[0]),
    )
    deltaY = (
        (endColorY[0] - startColor[0]) / float(size[0]),
        (endColorY[1] - startColor[1]) / float(size[0]),
        (endColorY[2] - startColor[2]) / float(size[0]),
    )

    thisPixelX = ()
    thisPixelY = ()

    for j in range(im.size[1]):  # for every pixel:
        if j != 0:
            thisPixelY = tf.addTuples(thisPixelY, deltaY)
        else:
            thispixelY = startColor

        for i in range(im.size[0]):
            if i == 0 and j == 0:
                thisPixelX = startColor
                thisPixelY = startColor
                pixels[i, j] = startColor
                continue
            if i != 0:
                thisPixelX = tf.addTuples(thisPixelX, deltaX)
            else:
                thisPixelX = startColor
            add = tf.divTuple(tf.addTuples(thisPixelY, thisPixelX), 2)
            pixels[i, j] = tf.roundTuple(add)

    # blur the background
    enhancer = ImageEnhance.Sharpness(im)
    factor = 0.05
    im = enhancer.enhance(factor)
    # brighten the colour
    enhancer = ImageEnhance.Brightness(im)
    factor = 1.5
    im = enhancer.enhance(factor)
    # im.save(title)

    return im


def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        # split the line by spaces to get words
        words = text.split(" ")
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ""
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
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
    font_file_path = settings.BASE_DIR.__str__() + "/static/fonts/YesevaOne.ttf"
    # font_file_path = BASE_DIR.__str__() +'/static/fonts/JosefinSans-SemiBold.ttf'
    # font_file_path = 'static/fonts/YesevaOne.ttf'
    # font = ImageFont.truetype(font_file_path, size=30, encoding="utf-8")
    # font = ImageFont.truetype(font_file_path, size=30)
    truetype_url = "https://github.com/googlefonts/josefinsans/blob/master/fonts/ttf/JosefinSans-Bold.ttf?raw=true"
    font = ImageFont.truetype(urlopen(truetype_url), size=30)
    (x, y) = (150, 480)
    color = "rgb(255, 055,05)"  # white color
    draw.text((x, y), name, fill=color, font=font, anchor="md")
    return image


def title(image, title):
    # image = Image.open(image)
    draw = ImageDraw.Draw(image)
    # create the ImageFont instance
    truetype_url = (
        "https://github.com/googlefonts/Fira/blob/main/ttf/FiraSans-Bold.ttf?raw=true"
    )
    font = ImageFont.truetype(urlopen(truetype_url), size=25)
    # font_file_path = 'static/fonts/FiraCode-SemiBold.ttf'
    # font = ImageFont.truetype(font_file_path, size=25)
    color = "rgb(255, 255, 255)"  # white color
    image_size = image.size
    lines = text_wrap(title, font, image_size[0] - 10)
    line_height = font.getsize("hg")[1]

    x = 150
    y = 400
    for line in lines:
        # draw the line on the image
        draw.text((x, y), line, fill=color, font=font, anchor="ms")

        # update the y position so that we can use it for next line
        y = y + line_height
    # save the image
    # img.save('word2.png', optimize=True)
    return image


def save(image, title):
    path = str(settings.MEDIA_ROOT) + "/generated/" + title + ".png"
    image.save(path, "PNG")
    return path
