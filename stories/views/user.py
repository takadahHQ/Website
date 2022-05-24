from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.db.models import Count
from stories.forms import StoryForm, ChapterForm

from stories.models import Chapters, Stories, Tag

class ShowStory(DetailView):
    template_name = 'reader/story_detail.html'
    context_object_name = 'story'

    def get_queryset(self):
        return Stories.objects.filter(slug=self.kwargs['slug']).exclude(status='pending').annotate(chapter_count=Count('chapters'))

class ShowChapter(DetailView):
    model = Chapters
    template_name = 'reader/read.html'
    context_object_name = 'story'

class ShowTag(TemplateView):
    model = Tag
    template_name = 'reader/read.html'
    context_object_name = 'story'

    def get_queryset(self):
        return Tag.objects.filter(name=self.request.user).order_by('-created_at')[:5]


