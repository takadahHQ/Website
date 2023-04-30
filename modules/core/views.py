from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from modules.stories.models import History
from .forms import SignUpForm, ProfileForm
from .models import Users, ContactUs
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    ListView,
    DeleteView,
    TemplateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .actions import (
    get_users_profile,
    homepage,
    get_bookmarks,
    get_histories,
    get_bookmarked_stories,
    get_profile,
)


def index(request):
    context = homepage(count=12)
    return render(request, "stories/index.html", context)


def error_500(request):
    return render(request, "core/error/500.html")


def error_404(request, exception):
    return render(request, "core/error/404.html")


def generatedCss(request):
    reply = render(request, "css.html", content_type="text/css")
    reply["type"] = "text/css"
    reply["mimetype"] = "text/css"
    return reply


class SignUpView(CreateView):
    model = Users
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ProfileView(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy("dashboard")
    template_name = "registration/update_profile.html"


class ShowBookmark(LoginRequiredMixin, ListView):
    template_name = "core/reader/bookmark.html"
    context_object_name = "bookmarks"
    paginate_at = 10

    def get_queryset(self):
        return get_bookmarks(user=self.request.user)


class ShowHistory(LoginRequiredMixin, ListView):
    template_name = "core/reader/history.html"
    context_object_name = "histories"

    def get_queryset(self):
        return get_histories(user=self.request.user)


class DeleteHistory(LoginRequiredMixin, DeleteView):
    model = History
    context_object_name = "histories"
    sucess_url = reverse_lazy("core:history")
    template_name = "core/reader/read.html"


class AuthorView(DetailView):
    # model: Users
    # queryset = Users.objects.filter(is_active=True).prefetch_related('author_user', 'editor','chapter_set')
    slug_field = "username"
    slug_url_kwarg = "username"
    context_object_name = "author"
    template_name = "core/user/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bookmarks, reviews = get_profile(user=self.kwargs.get("username", None))
        context["bookmarks"] = bookmarks
        context["reviews"] = reviews
        return context

    def get_object(self):
        slug = self.kwargs.get("username")
        # query = get_object_or_404(
        #     Users,
        #     username__iexact=slug,
        # )
        query = Users.objects.filter(
            username__iexact=slug,
        )  # .prefetch_related("authors", "editors", "authors__story")
        return Users.objects.get_by_natural_key(username=slug)


class FeeView(TemplateView):
    template_name = "pages/pricing.html"


class ContactView(TemplateView):
    template_name = "pages/contact.html"


# @method_decorator(csrf_exempt, name="dispatch")
class ContactUsView(View):
    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # create a new ContactUs object with the received data
        contact = ContactUs.objects.create(name=name, phone=phone, message=message)

        # return a response indicating successful submission
        return HttpResponse("Thank you for your message!")

    def get(self, request):
        return render(request, "pages/contact.html")


class CareersView(TemplateView):
    template_name = "pages/careers.html"


class AboutView(TemplateView):
    template_name = "pages/about.html"
