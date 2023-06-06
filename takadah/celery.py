import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "takadah.settings")
app = Celery("takadah")
app.autodiscover_tasks()
