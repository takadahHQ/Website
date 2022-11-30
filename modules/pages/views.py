from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Page

def index(request):
    return HttpResponse("Hello, to the pages application")

def page(request, path=None, slug=None):
    if(path != None):
        path = get_object_or_404(Page, slug=path)
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'pages/page.html', {'page':page})