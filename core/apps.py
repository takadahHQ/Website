from django.apps import AppConfig
from watson import search as watson

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

def ready(self):
        users = self.get_model("Users", fields=("username", "first_name", "last_name", "pseudonym", "bio"))
        watson.register(users)