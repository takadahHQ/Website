from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from modules.subscriptions.models import Sponsor, Package


class SponsorListView(ListView):
    model = Sponsor
    template_name = "sponsorship/sponsor_list.html"


class SponsorCreateView(CreateView):
    model = Sponsor
    fields = "__all__"
    template_name = "sponsorship/sponsor_form.html"
    success_url = reverse_lazy("sponsorship:sponsor-list")


class SponsorUpdateView(UpdateView):
    model = Sponsor
    fields = "__all__"
    template_name = "sponsorship/sponsor_form.html"
    success_url = reverse_lazy("sponsorship:sponsor-list")


class SponsorDeleteView(DeleteView):
    model = Sponsor
    template_name = "sponsorship/sponsor_confirm_delete.html"
    success_url = reverse_lazy("sponsorship:sponsor-list")
