from django.conf import settings
# from django.core.cache import DEFAULT_CACHE_ALIAS
from user_agents import parse


# # `get_cache` function has been deprecated since Django 1.7 in favor of `caches`.
# try:
#     from django.core.cache import caches

#     def get_cache(backend, **kwargs):
#         return caches[backend]
# except ImportError:
#     from django.core.cache import get_cache


def getUserAgent(request):
    if not hasattr(request, 'META'):
        return ''

    ua_string = request.META.get('HTTP_USER_AGENT', '')#new one 
    #new below
    #ua_string =  request.META['HTTP_USER_AGENT']

    if not isinstance(ua_string, text_type):
        ua_string = ua_string.decode('utf-8', 'ignore')

    user_agent = parse(ua_string)
    return user_agent

def getClientIp(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def getReferrer(request):
    referer = request.META.get('HTTP_REFERER')
    return referer

def getLocale(self):
def getContinentName(self):
def getContinentCode(self):
def getCountryName(self):
def getCountryCode(self):
def getPostalCode(self):
def getCityName(self):
def getTimeZone(self):



def getAndSetUserAgent(request):
    # If request already has ``user_agent``, it will return that, otherwise
    # call get_user_agent and attach it to request so it can be reused
    if hasattr(request, 'user_agent'):
        return request.user_agent

    if not request:
        return parse('')

    request.user_agent = get_userAgent(request)
    return request.user_agent