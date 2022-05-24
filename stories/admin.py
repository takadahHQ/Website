import imp
from django.contrib import admin
from .models import Stories, Categories, Chapters, Characters, Bookmarks, Genres, Languages, Ratings, Universes, Tag, Types
# Register your models here.


admin.site.register(Tag)
admin.site.register(Types)
admin.site.register(Categories)
admin.site.register(Genres)
admin.site.register(Languages)
admin.site.register(Ratings)
admin.site.register(Bookmarks)
admin.site.register(Stories)
admin.site.register(Chapters)
admin.site.register(Characters)
admin.site.register(Universes)
