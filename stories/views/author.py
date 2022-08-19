from pprint import pprint
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, TemplateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views import View
# from django.db.models import Count
from django.db.models import Avg, Count
from stories.forms import AuthorForm, EditorForm, StoryForm, ChapterForm, CharacterForm
from stories.models import Chapter, Stories, Character, Author, Editor
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
from django.conf import settings

class CharacterInline(InlineFormSetFactory):
    model = Character
    fields = ['name', 'category']

class AuthorInline(InlineFormSetFactory):
    model = Author
    fields = ['story', 'user']
    extra = 1

class EditorInline(InlineFormSetFactory):
    model = Editor
    fields = ['story', 'user']

class storyDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'stories/dashboard.html'
    model = Stories

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['total_likes'] = self.total_likes()
        context['published'] = self.story_list()
        context['stats'] = self.story_stats()
        return context

    def total_likes(self):
        #liked = Stories.objects.filter(authors=self.request.user).annotate(total_likes=Sum(likes))
        likes = Stories.objects.filter(author=self.request.user).aggregate(total_likes=Count('likes'))['total_likes']
        #all_stories = self.request.user.authors.all()
        #stotal_likes_received = all_stories.aggregate(total_likes=Count('likes'))['total_likes']
        return likes

    def story_list(self):
       story =  Stories.objects.exclude(status='pending').exclude(status='draft').filter(author=self.request.user)
       return story

    def story_stats(self):
        stats = {'views': {'result': 1234, 'updated': '2 hours ago'}, 'likes': {'result': 63689, 'updated': '2 minutes ago'}, 'dislikes': {'result': 1234, 'updated': '21 days ago'}, 'reviews': {'result': 44748534, 'updated': '2 seconds ago'}}
        return stats

class viewStory(LoginRequiredMixin, DetailView):
    template_name = 'stories/authors/story_detail.html'
    context_object_name = 'story'
    model = Stories

# class storyList(LoginRequiredMixin, ListView):
#     template_name = 'stories/list_stories.html'
#     model = Stories
#     context_object_name = 'stories'

#     def get_queryset(self):
#         return Stories.objects.filter(author =self.request.user)#.annotate(word_count)

class storyList(LoginRequiredMixin, ListView):
    template_name = 'stories/authors/list_stories.html'
    model = Stories
    context_object_name = 'stories'

    def get_queryset(self):
        return Stories.objects.filter(author =self.request.user)

def update_author(request, pk):
    author = Author.objects.get(id=pk)
    form = AuthorForm(request.POST or None, instance=author)
    if request.method =="POST":
        if form.is_valid():
            author = form.save()
            return redirect("author:detail-author", pk=author.id)
    context = {
        "aform": form,
        "author": author,
    }
    return render(request, "stories/partials/author_form.html", context)

def detail_author(request, pk):
    author = Author.objects.get(id=pk)
    context = {
        "author": author,
    }
    return render(request, "stories/partials/author_details.html", context)

def delete_author(request, pk):
    author = Author.objects.get(id=pk)
    author.delete()
    return HttpResponse('')

def save_author(request, pk):
    story = Stories.objects.get(id=pk)
    authors = Author.objects.filter(story=story)
    form = AuthorForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            author = form.save(commit=False)
            author.story = story
            author.save()
            return redirect("author:detail-author", pk=story.id)
        else:
            return render(request, "stories/partials/add_author.html", context={"aform": form})
    else:
        return render(request, "stories/partials/add_author.html", context={"aform": form,        "story": story,
        "authors": authors,})

def add_editor(request):
    # story = Stories.objects.get(id=pk)
    # form = EditorForm()

    # if request.method == "POST":
    #     if form.is_valid():
    #         editor = form.save(commit=False)
    #         editor.story = story
    #         editor.save()
    #         return HttpResponse("success")
    #     else:
    #         return render(request, "partials/editor_form.html", context={"editorform": form})

    context = {
        "eform": EditorForm(),
    }

    return render(request, "stories/partials/add_editor.html", context)

def add_character(request):
    #story = Stories.objects.get(id=pk)
    #characters = Character.objects.filter(story=story)

    form = CharacterForm()

    # if request.method == "POST":
    #     if form.is_valid():
    #         character = form.save(commit=False)
    #         character.story = story
    #         character.save()
    #         return HttpResponse("success")
    #     else:
    #         return render(request, "partials/author_form.html", context={ "cform": CharacterForm()})

    context = {
        "cform": CharacterForm()
    }

    return render(request, "stories/partials/add_character.html", context={ "cform": form})




# def add_character(request, pk):
#     story = Stories.objects.get(id=pk)
#     characters = Character.objects.filter(story=story)

#     form = AuthorForm(request.POST or None)

#     if request.method == "POST":
#         if form.is_valid():
#             character = form.save(commit=False)
#             character.story = story
#             character.save()
#             return HttpResponse("success")
#         else:
#             return render(request, "partials/author_form.html", context={"authorform": form})

#     context = {
#         "cform": form,
#         "story": story,
#         "characters": characters
#     }

#     return render(request, "add_author.html", context)
# #create a formset page with functions
# def newStory(request):
#     form = StoryForm(request.Post or None)
#     characterset = 
#     authorset = 
# if request.method == 'POST':
#     if formset.is_valid():
#         formset.instance = story
#         formset.save()
#         return redirect("author:show", pk=story.id)

#     context = {
#         "characterset": characterset
#     }

#     return render(request, 'stories/create_story.html', context)

class createStory(LoginRequiredMixin, CreateView):
    template_name = 'stories/authors/create_story.html'
    model = Stories
    form_class = StoryForm

    def get_success_url(self):
        return reverse_lazy('author:update', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.save()
        form.instance.author.add(self.request.user)
        return super().form_valid(form)

class updateStory(LoginRequiredMixin, UpdateView):
    template_name = "stories/authors/edit_story.html"
    model = Stories
    form_class = StoryForm

    def get_success_url(self):
        return reverse_lazy('author:show', kwargs={'pk': self.object.pk})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['story'] = self.object
        context['author'] = Author.objects.filter(story=self.object.pk)
        return context


class deleteStory(LoginRequiredMixin, DeleteView):
    template_name = "stories/authors/delete_story.html"
    model = Stories
    success_url = reverse_lazy('author:list')

class createChapter(LoginRequiredMixin,CreateView):
    model = Chapter
    form_class = ChapterForm
   # success_url = reverse_lazy('login')
    template_name = "stories/chapters/create_chapter.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.edited_by = self.request.user
        form.instance.story = Stories.objects.get(id=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['story'] = Stories.objects.get(id=self.kwargs.get('pk'))
        return context

class updateChapter(LoginRequiredMixin, UpdateView):
    template_name = "stories/chapters/edit_chapter.html"
    model = Chapter
    form_class = ChapterForm

    def form_valid(self, form):
        form.instance.edited_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['story'] = self.object.story
        return context
  #  success_url = reverse_lazy('dashboard')

class deleteChapter(LoginRequiredMixin, DeleteView):
    template_name = 'sstories/chapters/delete_story.html'
    model = Chapter
    success_url = reverse_lazy('author:list')