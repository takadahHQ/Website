from django import template

from ..utils import getAndSetUserAgent


register = template.Library()


@register.filter()
def is_mobile(request):
    return getAndSetUserAgent(request).is_mobile


@register.filter()
def is_pc(request):
    return getAndSetUserAgent(request).is_pc


@register.filter()
def is_tablet(request):
    return getAndSetUserAgent(request).is_tablet


@register.filter()
def is_bot(request):
    return getAndSetUserAgent(request).is_bot


@register.filter()
def is_touch_capable(request):
    return getAndSetUserAgent(request).is_touch_capable
