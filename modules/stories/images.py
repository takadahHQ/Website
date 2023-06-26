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
    startColor = (
        random.randrange(1, 66),
        random.randrange(1, 255),
        random.randrange(1, 255),
    )
    endColorX = (
        random.randrange(1, 65),
        random.randrange(1, 255),
        random.randrange(1, 255),
    )
    endColorY = (
        random.randrange(1, 255),
        random.randrange(1, 65),
        random.randrange(1, 255),
    )
    size = (372, 512)

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
    # Load and paste the logo onto the image
    logo_url = (
        "https://takadahmedia.s3.amazonaws.com/static/images/android-chrome-512x512.png"
    )
    logo = Image.open(urlopen(logo_url)).convert("RGBA")
    # logo = logo.resize(size)

    # Calculate the position to paste the logo
    x = 0
    y = 0

    # Reduce the opacity of the logo by 60%
    factor = 0.4
    faded_logo = logo.copy()
    faded_logo.putalpha(int(255 * factor))
    # Create a blank image with the same size as the logo
    logo_bg = Image.new("RGBA", faded_logo.size, (0, 0, 0, 0))

    # Paste the transparent logo onto the logo background
    logo_bg.paste(faded_logo, (0, 0), mask=faded_logo)

    # Paste the blended logo onto the image
    im.paste(logo_bg, (x, y), mask=logo_bg)
    # Remove the black overlay look on the image
    enhancer = ImageEnhance.Brightness(im)
    factor = 1.2  # Increase the brightness factor to make the image brighter
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
    color = "rgb(255, 055,05)"  # white color
    border = "black"
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
    for line in lines:
        while font.getbbox(line)[2] < image.size[0] + 20:
            font = ImageFont.truetype(urlopen(truetype_url), size=font.size + 1)
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
