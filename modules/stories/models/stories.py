from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify
from modules.stories import images as img
from django.core.files import File
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager
from modules.stories.converter import h_encode
from versatileimagefield.fields import VersatileImageField
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from modules.stats.models import Service, Hit
from django.contrib.contenttypes.models import ContentType
from django.db.models import (
    Avg,
    Count,
    Max,
    Min,
    Func,
    F,
    DateTimeField,
    ExpressionWrapper,
)

try:
    mindsdb = __import__("mindsdb")
except ImportError:
    mindsdb = None

from flag.models import Flag
from modules.stories.models.include import (
    idModel,
    timeStampModel,
    CacheInvalidationMixin,
    CachedQueryManager,
)

# from modules.stories.models import History
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Stories(CacheInvalidationMixin, idModel, timeStampModel):
    status_choices = (
        ("abandoned", "Abandoned"),
        ("complete", "Complete"),
        ("hiatus", "Hiatus"),
        ("prerelease", "Pre-Released"),
        ("published", "Published"),
        ("oneshot", "One Shot"),
        ("ongoing", "Ongoing"),
        ("draft", "Draft"),
    )
    title = models.CharField(max_length=255, help_text="This is the book title")
    slug = models.SlugField(null=True, unique=True)
    abbreviation = models.CharField(
        max_length=15,
        unique=True,
        help_text="The abbreviation of the book title, e.g. Lord of the Rings would be LotR",
    )
    summary = RichTextField("synopsis", help_text="This is the summary of your book")
    cover = VersatileImageField(
        max_length=255,
        blank=True,
        null=True,
    )
    story_type = models.ForeignKey("Type", on_delete=models.CASCADE)
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="story_followers",
        symmetrical=False,
    )
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="story_likes"
    )
    dislikes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="story_dislike"
    )
    author = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="Author", related_name="authors", blank=True
    )
    translator = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="Translator",
        related_name="translators",
        blank=True,
    )
    editor = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="Editor", related_name="editors", blank=True
    )
    language = models.ForeignKey("Language", on_delete=models.CASCADE)
    genre = models.ManyToManyField("Genre", blank=True)
    characters = models.ManyToManyField("Character", related_name="names", blank=True)
    rating = models.ForeignKey(
        "Rating", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    released_at = models.DateTimeField()
    featured = models.BooleanField(default=False)
    featured_at = models.DateTimeField(blank=True, null=True)
    tags = TaggableManager()
    flags = GenericRelation(Flag)
    status = models.CharField(max_length=100, choices=status_choices, default="draft")
    service = GenericRelation(Service, related_query_name="story")

    objects = CachedQueryManager()

    def __str__(self):
        return self.title

    # @admin.display(description='Following')
    def following_count(self):
        return self.following.count()

    # .display(description='Follower')
    def followers_count(self):
        return self.followers.count()

    # #@admin.display(description='Likes')
    def likes_count(self):
        return self.likes.count()

    # #@admin.display(description='Dislikes')
    def dislikes_count(self):
        return self.dislikes.count()

    # #@admin.display(description='First chapter of Story')
    def get_read_guest(self):
        # hack to get it to work
        if self.chapters.first():
            return self.chapters.first().get_absolute_url()

    def get_read_user(self, request):
        pass
        # story = History.objects.filter(user=request.user).get(story=self.story)
        # return story.chapter.get_absolute_url()

    def create_cover(self):
        name = self.author.first().name()
        file = img.make(name, self.title, self.slug)
        filename = self.slug + ".png"
        self.cover.save(filename, File(file), save=True)
        return self.cover

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify("-".join([self.abbreviation, self.title]))
        # if not self.cover:
        #     self.cover = self.create_cover()

        super(Stories, self).save(*args, **kwargs)

    def get_cover(self):
        if not self.cover:
            self.cover = self.create_cover()
            test = self.cover.url
            return self.cover.thumbnail["200x200"].url
        else:
            return self.cover.thumbnail["400x200"].url

    def get_first_cover(self):
        if not self.cover:
            self.cover = self.create_cover()
            test = self.cover.url
            return self.cover.thumbnail["400x200"].url
        else:
            return self.cover.thumbnail["400x200"].url

    def get_meta_cover(self):
        if not self.cover:
            self.cover = self.create_cover()
            test = self.cover.url
            return self.cover.thumbnail["400x209"].url
        else:
            return self.cover.thumbnail["400x209"].url

    def get_story_cover(self):
        if not self.cover:
            self.cover = self.create_cover()
            test = self.cover.url
            return self.cover.url
        else:
            return self.cover.url

    def id(self):
        id = h_encode(self.id)
        print(id)
        return id

    def get_absolute_url(self):
        story_type = self.story_type.slug
        return reverse(
            "stories:show",
            kwargs={"type": story_type, "slug": self.slug},
        )

    def get_word_count(self):
        active_chapters = self.chapters.filter(
            status="active", released_at__lte=timezone.now()
        )
        total_word_count = sum(chapter.words for chapter in active_chapters)
        return total_word_count

    def create_service_for_stories(self):
        # Check if the story has a status of "published"
        # if self.status == "published":
        try:
            # Check if a service is already associated with the story
            service = self.service.get()
        except Service.DoesNotExist:
            # Get the ContentType of the Stories model
            stories_content_type = ContentType.objects.get_for_model(Stories)
            # Create a service instance for the story if not already associated
            service = Service.objects.create(
                name=self.title,
                link=self.get_absolute_url(),  # Set the link field using get_absolute_url()
                content_type=stories_content_type,
                object_id=self.id,
                # Set other relevant fields here for the Service model
                # ...
            )
            self.service.add(service)

    def get_chapter_analytics(self):
        # Get all chapters of the story
        chapters = self.chapters.all()

        # Initialize data structures to store analytics
        analytics_data = {
            "hits_per_chapter": [],
            "total_hits": 0,
            "locations_per_chapter": [],
            "time_of_view_per_chapter": [],
        }

        # Loop through each chapter to gather analytics data
        for chapter in chapters:
            # Get hits for the chapter
            hits = Hit.objects.filter(
                session__service__story=self,
                session__service__story__chapters=chapter,
            )

            # Calculate hits per chapter
            hits_count = hits.count()
            analytics_data["hits_per_chapter"].append(
                {"chapter": chapter, "hits": hits_count}
            )

            # Update total hits count
            analytics_data["total_hits"] += hits_count

            # Get locations of hits for the chapter
            locations = hits.values("location").annotate(count=models.Count("location"))
            analytics_data["locations_per_chapter"].append(
                {"chapter": chapter, "locations": locations}
            )

            # Calculate time of view per chapter
            time_of_view = hits.aggregate(total_time=models.Sum("duration"))[
                "total_time"
            ]
            analytics_data["time_of_view_per_chapter"].append(
                {"chapter": chapter, "time_of_view": time_of_view}
            )

        return analytics_data

    def get_story_analytics(self):
        service = self.service.first()
        # Get the best reading day
        # best_reading_day = (
        #     if service.get_views_by_days() is not None:
        #         service.get_views_by_days()
        #     else:
        #         "Sunday"
        # )

        if service:
            best_reading_day = service.get_views_by_days()
            # Get the views by location
            views_by_location = service.get_views_by_location()

            # Get the views by devices
            views_by_devices = service.get_views_by_device()

            # Get the best and worst time for all records
            best_time = service.get_most_active_hour()

            worst_time = service.get_least_active_hour()
        else:
            best_reading_day = ""
            # Get the views by location
            views_by_location = ""
            # Get the views by devices
            views_by_devices = ""
            # Get the best and worst time for all records
            best_time = ""
            worst_time = ""
        # Get the total amount of views
        total_views = 100

        return {
            "best_reading_time": best_time,
            "best_reading_day": best_reading_day,
            "total_views": total_views,
            "views_by_location": views_by_location,
            "views_by_devices": views_by_devices,
            "best_time": best_time,
            "worst_time": worst_time,
        }

    class Meta:
        verbose_name_plural = "stories"
        app_label = "stories"
