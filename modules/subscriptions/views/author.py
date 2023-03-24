from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from modules.stories.models import Stories
from modules.subscriptions.models.sponsor import Sponsors
from modules.subscriptions.models.package import Packages
from modules.subscriptions.actions.authors import get_packages


class SponsorListView(ListView):
    model = Sponsors
    template_name = "sponsorship/sponsor_list.html"


# class SponsorCreateView(CreateView):
#     model = Sponsors
#     fields = "__all__"
#     template_name = "sponsorship/sponsor_form.html"
#     success_url = reverse_lazy("sponsor:author:sponsor-list")


# class SponsorUpdateView(UpdateView):
#     model = Sponsors
#     fields = "__all__"
#     template_name = "sponsorship/sponsor_form.html"
#     success_url = reverse_lazy("sponsor:author:sponsor-list")


# class SponsorDeleteView(DeleteView):
#     model = Sponsors
#     template_name = "sponsorship/sponsor_confirm_delete.html"
#     success_url = reverse_lazy("sponsor:author:sponsor-list")


class PackageListView(ListView):
    model = Packages
    context_object_name = "packages"
    template_name = "sponsorship/package_list.html"

    def get_queryset(self):
        story = self.kwargs.get("story")
        user = self.request.user
        return get_packages(story=story, user=user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["story"] = self.kwargs.get("story")
        return context


class PackageCreateView(CreateView):
    model = Packages
    fields = ["name", "amount", "advance", "status"]
    template_name = "sponsorship/package_form.html"
    # success_url = reverse_lazy("sponsor:author:package-list")

    def get_success_url(self) -> str:
        super().get_success_url()
        story = self.kwargs.get("story")
        return reverse_lazy("sponsor:author:package-list", kwargs={"story": story})

    def form_valid(self, form):
        story = Stories.objects.get(id=self.kwargs.get("story"))
        form.instance.user = self.request.user
        form.instance.story = story
        return super().form_valid(form)


class PackageUpdateView(UpdateView):
    model = Packages
    fields = ["name", "amount", "advance", "status"]
    template_name = "sponsorship/package_form.html"

    def get_success_url(self) -> str:
        super().get_success_url()
        story = self.kwargs.get("story")
        return reverse_lazy("sponsor:author:package-list", kwargs={"story": story})


class PackageDeleteView(DeleteView):
    model = Packages
    template_name = "sponsorship/package_confirm_delete.html"

    def get_success_url(self) -> str:
        super().get_success_url()
        story = self.kwargs.get("story")
        return reverse_lazy("sponsor:author:package-list", kwargs={"story": story})
