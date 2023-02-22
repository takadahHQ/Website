from .storyid import Storyids

storyids = Storyids(min_length=12)


def h_encode(id):
    return storyids.encode(id)


def h_decode(h):
    z = storyids.decode(h)
    if z:
        return z


class StoryIdConverter:
    regex = "[0-9]+"

    def to_python(self, value):
        return h_decode(value)

    def to_url(self, value):
        return h_encode(value)
