from django.shortcuts import render
from requests import request

from stories.models import Bookmarks, History, Stories
from .forms import SignUpForm, ProfileForm
from .models import Users
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    #return HttpResponse("Hello, to the stories application")
    exclude = ['draft', 'prerelease']
    weekly = Stories.objects.filter(featured=True).filter(status='active')[:12]
    fresh = Stories.objects.order_by('created_at').exclude(status__in=exclude)[:12]
    completed = Stories.objects.filter(status='completed')[:12]
    return render(request, 'stories/index.html', {'weekly': weekly, 'fresh': fresh, 'completed': completed})

def generatedCss(request):
    reply = render(request, 'css.html')
    reply['type'] = 'text/css'
    return reply


class SignUpView(CreateView):
    model = Users
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

class ProfileView(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('dashboard')
    template_name = "registration/update_profile.html"


class ShowBookmark(LoginRequiredMixin, ListView):
    template_name = 'reader/bookmark.html'
    context_object_name = 'bookmarks'
    paginate_at = 10

    def get_queryset(self):
        return Bookmarks.objects.filter(user=self.request.user).order_by('-created_at')

class ShowHistory(LoginRequiredMixin, ListView):
    template_name = 'reader/history.html'
    context_object_name = 'histories'

    def get_queryset(self):
        return History.objects.filter(user=self.request.user).order_by('-created_at')

class DeleteHistory(LoginRequiredMixin, DeleteView):
    model = History
    context_object_name = 'histories'
    sucess_url = reverse_lazy('core:history')

class ShowStory(DetailView):
    template_name = 'reader/story_detail.html'

class ShowChapter(DetailView):
    template_name = 'reader/read.html'
