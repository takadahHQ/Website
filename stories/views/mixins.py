from stories.models import Stories, Chapters, History, Bookmarks
from django.http import HttpResponse 
import logging

class HistoryMixin(object):


    def dispatch(self, request, *args, **kwargs):
        if  request.user.is_authenticated:
            story = Chapters.objects.filter(slug=self.kwargs['slug'])
            History.objects.update_or_create(
                story=story.story,
                user= request.user,
                defaults={
                'story': story.story.id,
                'chapter': story.position,
                'user': request.user,
                'url': story.get_absolute_url(),
                'status': 'active',
    			})
        return super().dispatch(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     story = context['story']
    #     History.objects.update_or_create(
    #             story=story.story,
    #             user= request.user,
    #             defaults={
    #             'story': story.story,
    #             'chapter': story.position,
    #             'user': request.user,
    #             'url':story.get_absolute_url(),
    #             'status': 'active',
    #             })
    #     return context