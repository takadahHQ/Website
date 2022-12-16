from __future__ import unicode_literals
from django.apps import AppConfig
from watson import search as watson


class StoriesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "modules.stories"

    def ready(self):
        stories = self.get_model("Stories")
        # watson.register(stories, fields=("title", "summary","abbreviation",))
        watson.register(stories)
