from django import template
from django.template.loader import render_to_string

register = template.Library()

@register.filter
def inject_advert(value, arg):

    # ad_code = []
    # ad_code.append(render_to_string("adsense/inarticle1.html"))
    # ad_code.append(render_to_string("adsense/inarticle2.html"))
    # ad_code.append(render_to_string("adsense/inarticle3.html"))
    # ad_code.append(render_to_string("adsense/inarticle4.html"))
    # ad_code.append(render_to_string("adsense/inarticle5.html"))
    # ad_code.append(render_to_string("adsense/inarticle6.html"))

    # # set adcode picker
    # j = 0
    # Render our adsense code placed in html file
    ad_code = render_to_string("adverts/ads.html")

    # Break down content into paragraphs
    paragraphs = value.split("</p>")

    # Check if paragraph we want to post after exists
    if arg < len(paragraphs):

        # Append our code before the following paragraph
        paragraphs[arg] = ad_code + paragraphs[arg]

        # Assemble our text back with injected adsense code
        value = "</p>".join(paragraphs)

    # Break down content into paragraphs
    # paragraphs = value.split("</p>")

    # # insert after every 5th paragraph
    # for i in range(len(paragraphs)):
    #     if i % 5 == 0:
    #         paragraphs[i] = paragraphs[i] + ad_code[j]
    #         if j < 5:
    #             j += 1
    #         value = "</p>".join(paragraphs)

    return value