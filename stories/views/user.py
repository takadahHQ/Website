from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.db.models import Count
from stories.forms import StoryForm, ChapterForm
from taggit.models import Tag
from stories.models import Chapter, Stories, Bookmark, Language, Genre, Rating,Type, Universe
from stories.views.mixins import HistoryMixin


def StoryLike(request, id):
    story = get_object_or_404(Stories, id=id)
    if story.likes.filter(id=request.user.id).exists():
        story.likes.remove(request.user)
        story.save()
    else:
        story.likes.add(request.user)
        story.save()

    return render(request, 'stories/partials/like.html', {'story': story})

def StoryDisLike(request, id):
    #use together with htmx
    story = get_object_or_404(Stories, id=id)
    if story.dislikes.filter(id=request.user.id).exists():
        story.dislikes.remove(request.user)
        story.save()
    else:
        story.dislikes.add(request.user)
        story.save()

    return render(request, 'stories/partials/dislike.html', {'story': story})

def StoryBookmark(request, id):
    story = get_object_or_404(Stories, id=id)
    bookmark = Bookmark.objects.update_or_create(story=story, user=request.user, defaults={'story': story, 'user':request.user,})
    bookmark.save()
    bookmarks = Bookmark.objects.get(story=id)
    #save the story, user, url(!optional) and status
    return render(request, 'stories/partials/bookmark.html', {'bookmark': bookmarks})


def StoryFollow(request, id):
    story = get_object_or_404(Stories, id=id)
    if story.following.filter(id=request.user.id).exists():
        story.following.remove(request.user)
        story.save()
    else:
        story.following.add(request.user)
        story.save()

    return render(request, 'stories/partials/following.html', {'story': story})

class ShowStory(DetailView):
    template_name = 'stories/readers/story_detail.html'
    context_object_name = 'story'

    def get_queryset(self):
        return Stories.objects.select_related('story_type', 'language','rating').filter(slug=self.kwargs['slug']).exclude(status='pending').annotate(chapter_count=Count('chapter'))

class ShowChapter(HistoryMixin, DetailView):
    model = Chapter
    template_name = 'stories/readers/read.html'
    context_object_name = 'story'

class ShowTag(ListView):
    model = Stories
    template_name = 'stories/tags.html'
    context_object_name = 'story'

    def get_queryset(self):
        return Stories.objects.filter(tags__slug__in=[self.kwargs.get('slug')])
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['tag'] = get_object_or_404(Tag, slug=self.kwargs.get('slug'))#Tag.objects.get(slug=self.kwargs.get('slug'))
        return context

class ShowGenre(ListView):
    model = Stories
    template_name = 'stories/genres.html'
    context_object_name = 'genres'

    def get_queryset(self):
        #Stories.objects.filter(stories__genre=self.kwargs.get('pk')).exclude(stories__status='pending')#.order_by('-created_at')[:15]
        return Stories.objects.exclude(status='pending').exclude(status='draft').filter(genre__slug=self.kwargs.get('slug'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['genre'] = get_object_or_404(Genre, slug=self.kwargs.get('slug'))#Tag.objects.get(slug=self.kwargs.get('slug'))
        return context

class ShowRating(ListView):
    model = Rating
    template_name = 'stories/ratings.html'
    context_object_name = 'story'

    def get_queryset(self):
        return Rating.objects.exclude(status='pending').exclude(status='draft').filter(rating__slug=self.kwargs.get('slug'))

class ShowType(ListView):
    model = Stories
    template_name = 'stories/type.html'
    context_object_name = 'story'

    def get_queryset(self):
        return Stories.objects.exclude(status='pending').exclude(status='draft').filter(story_type__slug=self.kwargs.get('slug'))
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['type'] = get_object_or_404(Type, slug=self.kwargs.get('slug'))#Tag.objects.get(slug=self.kwargs.get('pk'))
        return context

class ShowLanguage(ListView):
    model = Language
    template_name = 'stories/language.html'
    context_object_name = 'story'

    def get_queryset(self):
        return Language.objects.exclude(status='pending').exclude(status='draft').filter(language__slug=self.kwargs.get('slug'))





