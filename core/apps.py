from django.apps import AppConfig
from watson import search as watson
from django.conf import settings

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

def ready(self):
    #users = self.get_model("Users", fields=("username", "first_name", "last_name", "pseudonym", "bio"))
    users = settings.AUTH_USER_MODEL
    watson.register(users)
    author = self.get_model("Users")
    watson.register(author)
    socials = self.get_model("Socials")
    watson.register(socials)