from modules.stories.models import Stories, Chapter, History
from django.http import HttpResponse
import logging


class UrlMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            chapter = Chapter.objects.get(slug=self.kwargs["slug"])
            History.objects.update_or_create(
                story=chapter.story,
                user=request.user,
                defaults={
                    "story": chapter.story,
                    "chapter": chapter,
                    "user": request.user,
                    "url": chapter.get_absolute_url(),
                    "status": "active",
                },
            )
        return super().dispatch(request, *args, **kwargs)
