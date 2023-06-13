from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser, UserManager
import secrets
from versatileimagefield.fields import VersatileImageField
from modules.stories.models import Review


def create_token():
    token = secrets.token_urlsafe(20)
    return token


class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = "{}__iexact".format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})


class Users(AbstractUser):
    gender_choices = (
        ("male", "Male"),
        ("female", "Female"),
        ("human", "Human"),
    )
    kyc_choices = (
        ("pending", "Pending Submission"),
        ("verification", "Pending Verification"),
        ("approved", "Approved"),
        ("declined", "Declined"),
    )
    pseudonym = models.CharField(max_length=255, blank=True, null=True)
    bio = RichTextField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_photo = VersatileImageField(max_length=2048, blank=True, null=True)
    following = models.ManyToManyField(
        "self", blank=True, related_name="followers", symmetrical=False
    )
    # created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=100, choices=gender_choices, default="human")
    kyc_status = models.CharField(max_length=100, choices=kyc_choices, default="active")
    kyc_verified_at = models.DateTimeField(blank=True, null=True)
    language = models.ForeignKey(
        "Languages", on_delete=models.CASCADE, blank=True, null=True
    )
    ref_code = models.CharField(max_length=20, blank=True)
    referrer = models.ForeignKey(
        "Users", on_delete=models.CASCADE, blank=True, null=True
    )
    active = models.BooleanField(default=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.name()

    def save(self, *args, **kwargs):
        if not self.id:
            self.ref_code = self.referral_code()
        if not self.ref_code:
            self.ref_code = self.referral_code()
        return super().save(*args, **kwargs)

    def referral_code(self):
        token = secrets.token_urlsafe(3)
        code = "%s%s" % (self.username[0:3], token)
        return code.strip()

    def get_referral_code(self):
        if not self.ref_code:
            self.ref_code = self.referral_code()
        return self.ref_code

    def get_profile_image(self):
        image = "https://api.dicebear.com/6.x/notionists/svg?seed=%s" % (self.username)
        return image

    def following_count(self):
        return self.following.count()

    def is_active(self):
        return self.active

    def followers_count(self):
        return self.followers.count()

    def name(self):
        if self.pseudonym:
            return self.pseudonym
        elif self.get_full_name():
            return self.get_full_name()
        else:
            return self.get_username()

    def get_absolute_url(self):
        return reverse_lazy("core:author", kwargs={"username": self.username.lower()})

    def total_stories_liked_by_other(self):
        return self.story_likes.exclude(author__author_user_in=self).count()

    def total_stories_disliked_by_other(self):
        return self.story_dislike.exclude(author__author_user_in=self).count()

    def total_stories_commented_by_other(self):
        return (
            Review.objects.filter(user=self, story__author_stories__user=self)
            .exclude(user=self)
            .count()
        )

    def total_stories_followed_by_other(self):
        return self.story_followers.exclude(author__author_user_in=self).count()

    def total_stories_followed_by_me(self):
        return self.story_followers.filter(author__author_user_in=self).count()

    def total_stories_disliked_by_me(self):
        return self.story_likes.filter(author__author_user_in=self).count()

    def total_stories_disliked_by_me(self):
        return self.story_dislike.filter(author__author_user_in=self).count()

    def total_stories_commented_by_me(self):
        return Review.objects.filter(
            user=self, story__author_stories__user=self
        ).count()

    class Meta:
        verbose_name_plural = "users"
        app_label = "core"
