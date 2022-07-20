import imp
from django.contrib import admin
from .models import Stories, Categories, Chapter, Character, Bookmark, Genre, Language, Rating, Universe, Tag, Type
# Register your models here.


admin.site.register(Tag)
admin.site.register(Type)
admin.site.register(Categories)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Rating)
admin.site.register(Bookmark)
admin.site.register(Stories)
admin.site.register(Chapter)
admin.site.register(Character)
admin.site.register(Universe)
