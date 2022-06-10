from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, TemplateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views import View
# from django.db.models import Count
from django.db.models import Avg, Count
from stories.forms import StoryForm, ChapterForm
from stories.models import Chapters, Stories, Characters
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory


class CharacterInline(InlineFormSetFactory):
    model = Characters
    fields = ['name', 'category']

class storyDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'stories/dashboard.html'
    model = Stories

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['total_likes'] = self.total_likes()

    def total_likes(self):
        #liked = Stories.objects.filter(authors=self.request.user).annotate(total_likes=Sum(likes))
        likes = Stories.objects.filter(authors=self.request.user).aggregate(total_likes=Count('likes'))['total_likes']
        #all_stories = self.request.user.authors.all()
        #stotal_likes_received = all_stories.aggregate(total_likes=Count('likes'))['total_likes']
        return likes

class viewStory(LoginRequiredMixin, DetailView):
    template_name = 'stories/show_story.html'
    context_object_name = 'story'
    model = Stories

class storyList(LoginRequiredMixin, ListView):
    template_name = 'stories/list_stories.html'
    model = Stories
    context_object_name = 'stories'

    def get_queryset(self):
        return Stories.objects.filter(authors=self.request.user)#.annotate(word_count)

class storyList(LoginRequiredMixin, ListView):
    template_name = 'stories/list_stories.html'
    model = Stories
    context_object_name = 'stories'

    def get_queryset(self):
        return Stories.objects.filter(authors=self.request.user)

  #  form_class = StoryForm
  #  success_url = reverse_lazy('story:addchapter')

class createStory(LoginRequiredMixin, CreateWithInlinesView):
    template_name = 'stories/create_story.html'
    model = Stories
    inlines = [CharacterInline]
    form_class = StoryForm
    success_url = reverse_lazy('author:list')

    def form_valid(self, form):
        form.instance.save()
        form.instance.authors.add(self.request.user)
        return super().form_valid(form)

class updateStory(LoginRequiredMixin, UpdateWithInlinesView):
    template_name = "stories/edit_story.html"
    model = Stories
    inlines = [CharacterInline]
    form_class = StoryForm
  #  success_url = reverse_lazy('dashboard')

class deleteStory(LoginRequiredMixin, DeleteView):
    #template_name = 'stories/create_story.html'
    model = Stories
    success_url = reverse_lazy('author:list')

class createChapter(LoginRequiredMixin,CreateView):
    model = Chapters
    form_class = ChapterForm
   # success_url = reverse_lazy('login')
    template_name = "stories/create_chapter.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class updateChapter(LoginRequiredMixin, UpdateView):
    template_name = "stories/edit_chapter.html"
    model = Chapters
    form_class = ChapterForm

    def form_valid(self, form):
        form.instance.edited_by = self.request.user
        return super().form_valid(form)
  #  success_url = reverse_lazy('dashboard')

class deleteChapter(LoginRequiredMixin, DeleteView):
    #template_name = 'stories/create_story.html'
    model = Stories
    success_url = reverse_lazy('author:list')