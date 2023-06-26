from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from urllib.request import urlopen
from io import BytesIO

# from django.contrib.staticfiles.storage import staticfiles_storage


def make(img_author, img_title, img_slug):
    bg = background()
    name = img_author
    cover = author(bg, name)
    titles = title(cover, img_title)
    save(titles, img_slug)


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
    phrases = [phrase.strip() for phrase in text.split(",")]

    for phrase in phrases:
        words = phrase.split(" ")
        i = 0
        current_line = ""
        while i < len(words):
            word = words[i]
            if font.getbbox(current_line + word)[2] <= max_width:
                current_line += word + " "
            else:
                if current_line:
                    lines.append(current_line.strip())
                current_line = word + " "
            i += 1

        if current_line:
            lines.append(current_line.strip())

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
    color = "rgb(31, 69,60)"  # white color
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
            stroke_width=1,
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
    # Automatically get the initial font size
    font = ImageFont.truetype(urlopen(truetype_url), size=0)
    while font.getbbox(title)[2] < (image.size[0]):
        font = ImageFont.truetype(urlopen(truetype_url), size=font.size + 1)

    color = "rgb(255, 255, 255)"  # white color
    border = "black"
    image_size = image.size
    lines = text_wrap(title, font, image_size[0] - 40)

    x = 186
    y = 112
    while font.getbbox(lines[0])[2] < image_size[0] - 40:
        width = ImageFont.truetype(urlopen(truetype_url), size=font.size + 1)
    for line in lines:
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

        line_height = font.getbbox("hg")[3] - font.getbbox("hg")[1]
        # update the y position so that we can use it for next line
        y = y + line_height
        width = width.getbbox(lines[0])[2] - 80
    return image


def save(image, title):
    path = title + ".png"
    image.save(path, format="PNG")
    print(path)


make("netesy", "Uzumaki Love", "uzumaki2")
make("netesy", "Legend of the Seeker, he who seeks, finds", "uzumaki-legend")
make("netesy", "Uzumaki Love", "uzumaki2")
make("netesy", "tested", "tested")
