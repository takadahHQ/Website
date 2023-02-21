from django.db.models import Q, Count, Sum, Prefetch
from django.shortcuts import get_object_or_404
from modules.core.models import Users
from modules.subscriptions.models import Sponsors, Packages
from modules.stories.models.stories import Stories
import pandas as pd
from itertools import chain
from django.db.models import CharField, Value as V
from django.db.models.functions import Concat

# from timezone import timezone
from django.utils import timezone

try:
    mindsdb = __import__("mindsdb")
except ImportError:
    mindsdb = None


# def get_sponsors(story: str, type: str):
#     get_sponsors
#     sponsors = (
#         Sponsors.objects.filter(~Q(status="pending") | ~Q(status="draft"))
#         .filter(package__story__slug=story)
#         .filter(package__story__story_type__slug=type)
#         .annotate(sponsors_count=Count("user"))
#         .select_related(
#             "user",
#             "package",
#         )
#     )
#     return sponsors


def can_view_sponsor(user: int, sponsor: int):
    try:
        sponsor = Sponsors.objects.get(user=user)
        story = Stories.object.get(pk=sponsor.package.story)
    except (Sponsors.DoesNotExist, Stories.DoesNotExist):
        return False
    return True


def get_sponsor(story: any, package: any, user: any = None):
    # check if can view the chapter else end it there
    if can_view_sponsor(user=user, sponsor=package):
        sponsor = Sponsors.objects.get(package__story__slug=story, pk=package)
        return sponsor


def get_sponsor_by_id(sponsor: int, user: any = None):
    if can_view_sponsor(user=user, sponsor=sponsor):
        sponsor = Sponsors.objects.filter(status="active").get(id=sponsor)
        return sponsor


def create_sponsor(story, chapter, text, user, parent):
    sponsor = Sponsors(
        story=story, chapter=chapter, user=user, text=text, parent=parent
    )
    sponsor.save()
    return sponsor


def update_sponsor(id, text):
    sponsor = Sponsors.objects.get(id=id)
    sponsor.text = text
    sponsor.save(update_fields=["text"])
    return sponsor


def get_sponsors(story: str, type: str):
    sponsors = (
        Sponsors.objects.filter(~Q(status="pending") | ~Q(status="draft"))
        .select_related("package", "user")
        .prefetch_related("package__name")
        .order_by("-created_at")
        .filter(package__story__slug=story)
    )

    if type:
        sponsors = sponsors.filter(package__story__story_type__slug=type)

    count = sponsors.count()
    return sponsors, count


def remove_sponsor(id: int):
    sponsor = Sponsors.objects.get(id=id)
    sponsor.delete()
    return True
