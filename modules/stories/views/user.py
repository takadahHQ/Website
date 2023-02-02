from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    ListView,
    TemplateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.db.models import Count
from modules.stories.actions.user import bookmark_story, get_all_ratings, get_language
from modules.stories.forms import StoryForm, ChapterForm
from taggit.models import Tag
from modules.stories.models import (
    Chapter,
    Stories,
    Bookmark,
    Language,
    Genre,
    Rating,
    Type,
    Universe,
)
from modules.stories.views.mixins import HistoryMixin
from modules.stories.actions import (
    get_genre,
    get_stories_by_genre,
    get_tag,
    get_stories_by_tag,
    get_type,
    get_stories_by_type,
    like_story,
    dislike_story,
    follow_story,
    get_story,
)


def storyLike(request, id):
    story = like_story(user=request.user, slug=id)
    return render(request, "stories/partials/like.html", {"story": story})


def storyDisLike(request, id):
    story = dislike_story(user=request.user, slug=id)
    return render(request, "stories/partials/dislike.html", {"story": story})


def storyBookmark(request, id):
    bookmarks = bookmark_story(user=request.user, slug=id)
    return render(request, "stories/partials/bookmark.html", {"bookmark": bookmarks})


def storyFollow(request, id):
    story = follow_story(user=request.user, slug=id)
    return render(request, "stories/partials/following.html", {"story": story})


# def showStory(request, id):
#     context = {}
#     template = ""
#     return render(request, template, context)


def showStory(request, type: str, slug: str):
    story = get_story(slug=slug, type=type)
    review = ""
    recommendation = ""
    context = {"story": story}
    template = "stories/readers/story_detail.html"
    return render(request, template, context)


# class ShowStory(DetailView):
#     template_name = "stories/readers/story_detail.html"
#     context_object_name = "story"

#     def get_queryset(self):
#         return get_story(slug=self.kwargs.get("slug"))


class ShowChapter(HistoryMixin, DetailView):
    model = Chapter
    template_name = "stories/readers/read.html"
    context_object_name = "story"


class ShowTag(ListView):
    model = Stories
    template_name = "stories/tags.html"
    context_object_name = "story"

    def get_queryset(self):
        return get_stories_by_tag(self.kwargs.get("slug"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["tag"] = get_tag(slug=self.kwargs.get("slug"))
        return context


class ShowGenre(ListView):
    model = Stories
    template_name = "stories/genres.html"
    context_object_name = "story"

    def get_queryset(self):
        # Stories.objects.filter(stories__genre=self.kwargs.get('pk')).exclude(stories__status='pending')#.order_by('-created_at')[:15]
        return get_stories_by_genre(slug=self.kwargs.get("slug"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["genre"] = get_genre(self.kwargs.get("slug"))
        return context


class ShowRating(ListView):
    model = Rating
    template_name = "stories/ratings.html"
    context_object_name = "story"

    def get_queryset(self):
        return get_all_ratings(slug=self.kwargs.get("slug"))


class ShowType(ListView):
    model = Stories
    template_name = "stories/type.html"
    context_object_name = "story"

    def get_queryset(self):
        return get_stories_by_type(self.kwargs.get("slug"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["type"] = get_type(self.kwargs.get("slug"))
        return context


class ShowLanguage(ListView):
    model = Language
    template_name = "stories/language.html"
    context_object_name = "story"

    def get_queryset(self):
        return get_language(self.kwargs.get("slug"))
