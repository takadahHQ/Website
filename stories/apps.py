from django.apps import AppConfig
from watson import search as watson


class StoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stories'

    def ready(self):
        stories = self.get_model("Stories")
        author = self.get_model("Author")
        watson.register(stories, fields=("title", "summary","abbreviation",))
        watson.register(author)
