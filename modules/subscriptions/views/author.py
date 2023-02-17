from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from modules.subscriptions.models.sponsor import Sponsors
from modules.subscriptions.models.package import Packages


class SponsorListView(ListView):
    model = Sponsors
    template_name = "sponsorship/sponsor_list.html"


# class SponsorCreateView(CreateView):
#     model = Sponsors
#     fields = "__all__"
#     template_name = "sponsorship/sponsor_form.html"
#     success_url = reverse_lazy("sponsorship:sponsor-list")


# class SponsorUpdateView(UpdateView):
#     model = Sponsors
#     fields = "__all__"
#     template_name = "sponsorship/sponsor_form.html"
#     success_url = reverse_lazy("sponsorship:sponsor-list")


# class SponsorDeleteView(DeleteView):
#     model = Sponsors
#     template_name = "sponsorship/sponsor_confirm_delete.html"
#     success_url = reverse_lazy("sponsorship:sponsor-list")


class PackageListView(ListView):
    model = Packages
    template_name = "sponsorship/package_list.html"


class PackageCreateView(CreateView):
    model = Packages
    fields = "__all__"
    template_name = "sponsorship/package_form.html"
    success_url = reverse_lazy("sponsorship:package-list")


class PackageUpdateView(UpdateView):
    model = Packages
    fields = "__all__"
    template_name = "sponsorship/package_form.html"
    success_url = reverse_lazy("sponsorship:package-list")


class PackageDeleteView(DeleteView):
    model = Packages
    template_name = "sponsorship/package_confirm_delete.html"
    success_url = reverse_lazy("sponsorship:package-list")
