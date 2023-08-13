# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404, redirect, render
# from django.urls import reverse_lazy
# from django.views.generic import (
#     CreateView,
#     UpdateView,
#     DetailView,
#     ListView,
#     TemplateView,
#     DeleteView,
# )
# from django.contrib.auth.mixins import LoginRequiredMixin

# # from django.views import View
# # from django.db.models import Count
# from django.db.models import Avg, Count
# from modules.stories.actions.authors import (
#     get_author_stories_reviews,
#     get_author_stories_views,
#     get_daily_earnings,
#     get_monthly_earnings,
#     get_weekly_earnings,
# )
# from modules.stories.forms import (
#     AuthorForm,
#     EditorForm,
#     StoryForm,
#     ChapterForm,
#     CharacterForm,
# )
# from modules.stories.models import Chapter, Stories, Character, Author, Editor
# from extra_views import (
#     CreateWithInlinesView,
#     UpdateWithInlinesView,
#     InlineFormSetFactory,
# )
# from django.conf import settings
# from modules.stories.actions import (
#     get_stories_by_author,
#     get_author_stories_likes,
#     get_author_stories_dislikes,
#     get_chapter,
# )
# from modules.stories.actions import (
#     get_reviews,
# )
# from modules.stories.mixins import AuthorRequiredMixin


# class CharacterInline(InlineFormSetFactory):
#     model = Character
#     fields = ["name", "category"]


# class AuthorInline(InlineFormSetFactory):
#     model = Author
#     fields = ["story", "user"]
#     extra = 1


# class EditorInline(InlineFormSetFactory):
#     model = Editor
#     fields = ["story", "user"]


# class storyDashboard(LoginRequiredMixin, TemplateView):
#     template_name = "stories/dashboard.html"
#     model = Stories

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["total_likes"] = self.total_likes()
#         context["published"] = self.story_list()
#         context["stats"] = self.story_stats()
#         context["earnings"] = self.story_earnings()
#         return context

#     def total_likes(self):
#         # liked = Stories.objects.filter(authors=self.request.user).annotate(total_likes=Sum(likes))
#         likes = Stories.objects.filter(author=self.request.user).aggregate(
#             total_likes=Count("likes")
#         )["total_likes"]
#         # all_stories = self.request.user.authors.all()
#         # stotal_likes_received = all_stories.aggregate(total_likes=Count('likes'))['total_likes']
#         return likes

#     def story_list(self):
#         #    story =  Stories.objects.exclude(status='pending').exclude(status='draft').filter(author__user__in=self.request.user)
#         story = get_stories_by_author(user=self.request.user)
#         return story

#     def story_stats(self):
#         likes = get_author_stories_likes(author=self.request.user)
#         dislikes = get_author_stories_dislikes(author=self.request.user)
#         reviews = get_author_stories_reviews(author=self.request.user)
#         views = get_author_stories_views(author=self.request.user)
#         stats = {
#             "views": {"result": views, "updated": "2 hours ago"},
#             "likes": {"result": likes, "updated": "2 minutes ago"},
#             "dislikes": {"result": dislikes, "updated": "21 days ago"},
#             "reviews": {"result": reviews, "updated": "2 seconds ago"},
#         }
#         return stats

#     def story_earnings(self):
#         daily = get_daily_earnings(author=self.request.user)
#         weekly = get_weekly_earnings(author=self.request.user)
#         monthly = get_monthly_earnings(author=self.request.user)
#         stats = {
#             "daily": {"amount": daily},
#             "weekly": {"amount": weekly},
#             "monthly": {"amount": monthly},
#         }
#         return stats


# class viewStory(AuthorRequiredMixin, LoginRequiredMixin, DetailView):
#     template_name = "stories/authors/story_detail.html"
#     context_object_name = "story"
#     model = Stories


# # class storyList(LoginRequiredMixin, ListView):
# #     template_name = 'stories/list_stories.html'
# #     model = Stories
# #     context_object_name = 'stories'

# #     def get_queryset(self):
# #         return Stories.objects.filter(author =self.request.user)#.annotate(word_count)


# class storyList(LoginRequiredMixin, ListView):
#     template_name = "stories/authors/list_stories.html"
#     model = Stories
#     context_object_name = "stories"

#     def get_queryset(self):
#         return Stories.objects.filter(author=self.request.user.id)


# def update_author(request, pk):
#     author = Author.objects.get(id=pk)
#     form = AuthorForm(request.POST or None, instance=author)
#     if request.method == "POST":
#         if form.is_valid():
#             author = form.save()
#             return redirect("stories:author:detail-author", pk=author.id)
#     context = {
#         "aform": form,
#         "author": author,
#     }
#     return render(request, "stories/partials/author_form.html", context)


# def detail_author(request, pk):
#     author = Author.objects.get(id=pk)
#     context = {
#         "author": author,
#     }
#     return render(request, "stories/partials/author_details.html", context)


# def delete_author(request, pk):
#     author = Author.objects.get(id=pk)
#     author.delete()
#     return HttpResponse("")


# def save_author(request, pk):
#     story = Stories.objects.get(id=pk)
#     authors = Author.objects.filter(story=story)
#     form = AuthorForm(request.POST or None)

#     if request.method == "POST":
#         if form.is_valid():
#             author = form.save(commit=False)
#             author.story = story
#             author.save()
#             return redirect("stories:author:detail-author", pk=story.id)
#         else:
#             return render(
#                 request, "stories/partials/add_author.html", context={"aform": form}
#             )
#     else:
#         return render(
#             request,
#             "stories/partials/add_author.html",
#             context={
#                 "aform": form,
#                 "story": story,
#                 "authors": authors,
#             },
#         )


# def add_editor(request):
#     # story = Stories.objects.get(id=pk)
#     # form = EditorForm()

#     # if request.method == "POST":
#     #     if form.is_valid():
#     #         editor = form.save(commit=False)
#     #         editor.story = story
#     #         editor.save()
#     #         return HttpResponse("success")
#     #     else:
#     #         return render(request, "partials/editor_form.html", context={"editorform": form})

#     context = {
#         "eform": EditorForm(),
#     }

#     return render(request, "stories/partials/add_editor.html", context)


# def add_character(request):
#     # story = Stories.objects.get(id=pk)
#     # characters = Character.objects.filter(story=story)

#     form = CharacterForm()

#     # if request.method == "POST":
#     #     if form.is_valid():
#     #         character = form.save(commit=False)
#     #         character.story = story
#     #         character.save()
#     #         return HttpResponse("success")
#     #     else:
#     #         return render(request, "partials/author_form.html", context={ "cform": CharacterForm()})

#     context = {"cform": CharacterForm()}

#     return render(
#         request, "stories/partials/add_character.html", context={"cform": form}
#     )


# # def add_character(request, pk):
# #     story = Stories.objects.get(id=pk)
# #     characters = Character.objects.filter(story=story)

# #     form = AuthorForm(request.POST or None)

# #     if request.method == "POST":
# #         if form.is_valid():
# #             character = form.save(commit=False)
# #             character.story = story
# #             character.save()
# #             return HttpResponse("success")
# #         else:
# #             return render(request, "partials/author_form.html", context={"authorform": form})

# #     context = {
# #         "cform": form,
# #         "story": story,
# #         "characters": characters
# #     }

# #     return render(request, "add_author.html", context)
# # #create a formset page with functions
# # def newStory(request):
# #     form = StoryForm(request.Post or None)
# #     characterset =
# #     authorset =
# # if request.method == 'POST':
# #     if formset.is_valid():
# #         formset.instance = story
# #         formset.save()
# #         return redirect("stories:author:show", pk=story.id)

# #     context = {
# #         "characterset": characterset
# #     }

# #     return render(request, 'stories/create_story.html', context)


# class createStory(LoginRequiredMixin, CreateView):
#     template_name = "stories/authors/create_story.html"
#     model = Stories
#     form_class = StoryForm

#     def get_success_url(self):
#         return reverse_lazy("stories:author:update", kwargs={"pk": self.object.id})

#     def form_valid(self, form):
#         # self.object = form.save()
#         #     # form.instance.save()
#         #     # form.instance.author.add(self.request.user)
#         # self.object.author.add(self.request.user)
#         # self.object.save()
#         return super().form_valid(form)


# class StoriesCreateView(LoginRequiredMixin, CreateView):
#     model = Stories
#     template_name = "stories/authors/create_story.html"
#     form_class = StoryForm

#     def get_success_url(self):
#         return reverse_lazy("stories:author:update", kwargs={"pk": self.object.id})

#     def form_valid(self, form):
#         # self.object = form.save()
#         # self.object.save()
#         form.instance.save()
#         form.instance.author.add(self.request.user)
#         # self.object.author.add(self.request.user)
#         # self.object.save()
#         form.instance.get_cover()
#         return super().form_valid(form)


# class updateStory(AuthorRequiredMixin, LoginRequiredMixin, UpdateView):
#     template_name = "stories/authors/edit_story.html"
#     model = Stories
#     form_class = StoryForm

#     def get_success_url(self):
#         return reverse_lazy("stories:author:show", kwargs={"pk": self.object.id})

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["story"] = self.object
#         context["author"] = Author.objects.filter(story=self.object.pk)
#         return context


# class deleteStory(AuthorRequiredMixin, LoginRequiredMixin, DeleteView):
#     template_name = "stories/authors/delete_story.html"
#     model = Stories
#     success_url = reverse_lazy("stories:author:list")


# class createChapter(AuthorRequiredMixin, LoginRequiredMixin, CreateView):
#     model = Chapter
#     form_class = ChapterForm
#     # success_url = reverse_lazy('login')
#     template_name = "stories/chapters/create_chapter.html"

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.edited_by = self.request.user
#         form.instance.story = Stories.objects.get(id=self.kwargs.get("pk"))
#         return super().form_valid(form)

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["story"] = Stories.objects.get(id=self.kwargs.get("pk"))
#         return context

#     def get_success_url(self):
#         return reverse_lazy(
#             "stories:author:preview-chapter",
#             kwargs={"pk": self.object.story.id, "slug": self.object.slug},
#         )


# class updateChapter(AuthorRequiredMixin, LoginRequiredMixin, UpdateView):
#     template_name = "stories/chapters/edit_chapter.html"
#     model = Chapter
#     form_class = ChapterForm

#     def get_object(self, queryset=None):
#         chapter = get_object_or_404(
#             Chapter, story__id=self.kwargs["pk"], slug=self.kwargs["slug"]
#         )
#         return chapter

#     def form_valid(self, form):
#         form.instance.edited_by = self.request.user
#         return super().form_valid(form)

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["story"] = self.object.story
#         return context

#     def get_success_url(self):
#         return reverse_lazy(
#             "stories:author:preview-chapter",
#             kwargs={"pk": self.object.story.id, "slug": self.object.slug},
#         )


# #  success_url = reverse_lazy('dashboard')


# class deleteChapter(AuthorRequiredMixin, LoginRequiredMixin, DeleteView):
#     template_name = "stories/chapters/delete_chapter.html"
#     model = Chapter
#     success_url = reverse_lazy("stories:author:list")

#     def get_object(self, queryset=None):
#         chapter = get_object_or_404(
#             Chapter, story__id=self.kwargs["pk"], slug=self.kwargs["slug"]
#         )
#         return chapter

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["story"] = self.object.story
#         return context


# class showChapter(AuthorRequiredMixin, LoginRequiredMixin, DetailView):
#     model = Chapter
#     template_name = "stories/authors/preview.html"
#     context_object_name = "story"

#     def get_object(self):
#         chapter = get_object_or_404(
#             Chapter, story__id=self.kwargs["pk"], slug=self.kwargs["slug"]
#         )
#         return chapter

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["reviewed"], context["reviews_count"] = get_reviews(
#             story=self.kwargs.get("story"), chapter=self.kwargs.get("slug")
#         )
#         return context
