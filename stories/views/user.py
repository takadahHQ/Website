from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.db.models import Count
from stories.forms import StoryForm, ChapterForm

from stories.models import Chapters, Stories, Tag
from stories.views.mixins import HistoryMixin


def StoryLike(request, pk):
    story = get_object_or_404(Stories, id=request.POST.get('blogpost_id'))
    if story.likes.filter(id=request.user.id).exists():
        story.likes.remove(request.user)
    else:
        story.likes.add(request.user)

    return HttpResponseRedirect(reverse('blogpost-detail', args=[str(pk)]))

def StoryDisLike(request, pk):
    story = get_object_or_404(Stories, id=request.POST.get('blogpost_id'))
    if story.dislikes.filter(id=request.user.id).exists():
        story.dislikes.remove(request.user)
    else:
        story.dislikes.add(request.user)

    return HttpResponseRedirect(reverse('blogpost-detail', args=[str(pk)]))

def StoryFollow(request, pk):
    story = get_object_or_404(Stories, id=request.POST.get('blogpost_id'))
    if story.following.filter(id=request.user.id).exists():
        story.following.remove(request.user)
    else:
        story.following.add(request.user)

    return HttpResponseRedirect(reverse('blogpost-detail', args=[str(pk)]))

class ShowStory(DetailView):
    template_name = 'reader/story_detail.html'
    context_object_name = 'story'

    def get_queryset(self):
        return Stories.objects.filter(slug=self.kwargs['slug']).exclude(status='pending').annotate(chapter_count=Count('chapters'))

class ShowChapter(HistoryMixin, DetailView):
    model = Chapters
    template_name = 'reader/read.html'
    context_object_name = 'story'

class ShowTag(TemplateView):
    model = Tag
    template_name = 'reader/read.html'
    context_object_name = 'story'

    def get_queryset(self):
        return Tag.objects.filter(name=self.request.user).order_by('-created_at')[:5]


