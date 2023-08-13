from django.apps import AppConfig
from watson import search as watson


class AnimeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.anime'
