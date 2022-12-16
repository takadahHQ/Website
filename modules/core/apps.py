from __future__ import unicode_literals
from django.apps import AppConfig
from watson import search as watson
from django.conf import settings


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "modules.core"

    def ready(self):
        author = self.get_model("Users")
        watson.register(
            author,
            fields=(
                "username",
                "first_name",
                "last_name",
                "pseudonym",
                "bio",
            ),
        )
        # watson.register(author)
