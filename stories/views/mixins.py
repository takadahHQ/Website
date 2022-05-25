from stories.models import Stories, Chapters, History, Bookmarks
from django.http import HttpResponse 
import logging

class HistoryMixin(object):


    def dispatch(self, request, *args, **kwargs):
        if  request.user.is_authenticated:
            chapter = Chapters.objects.get(slug=self.kwargs['slug'])
            History.objects.update_or_create(
                story=chapter.story,
                user= request.user,
                defaults={
                'story': chapter.story,
                'chapter': chapter,
                'user': request.user,
                'url': chapter.get_absolute_url(),
                'status': 'active',
    			})
        return super().dispatch(request, *args, **kwargs)