from datetime import timezone
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from modules.subscriptions.models import Sponsors, Packages
from django.http import HttpResponseRedirect
from django.urls import reverse
from dotenv import load_dotenv
import os

import stripe


class SponsorListView(ListView):
    model = Sponsors
    template_name = "sponsorship/sponsor_list.html"


class SponsorCreateView(CreateView):
    model = Sponsors
    fields = "__all__"
    template_name = "sponsorship/sponsor_form.html"
    success_url = reverse_lazy("sponsorship:sponsor-list")


class SponsorUpdateView(UpdateView):
    model = Sponsors
    fields = "__all__"
    template_name = "sponsorship/sponsor_form.html"
    success_url = reverse_lazy("sponsorship:sponsor-list")


class SponsorDeleteView(DeleteView):
    model = Sponsors
    template_name = "sponsorship/sponsor_confirm_delete.html"
    success_url = reverse_lazy("sponsorship:sponsor-list")


def sponsor(request, story, slug):
    package = Packages.objects.get(slug=slug)

    stripe.api_key = os.environ.get("STRIPE_KEY")
    stripe_session = stripe.checkout.Session.create(
        customer_email=request.user.email,  # Set customer email here
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": package.name,
                        "description": package.story.title,
                        "images": [package.story.get_cover()],
                    },
                    "unit_amount": package.amount
                    * 100,  # Stripe requires amount in cents
                    "recurring": {
                        "interval": "month",
                        "interval_count": 1,
                    },
                },
                "quantity": 1,
            }
        ],
        mode="subscription",
        success_url=request.build_absolute_uri(
            reverse(
                "sponsor:sponsor-success",
                kwargs={
                    "story": story,
                    "ref": "{CHECKOUT_SESSION_ID}?payment_intent={PAYMENT_INTENT_ID}",
                },
            )
        ),
        cancel_url=request.build_absolute_uri(
            reverse(
                "sponsor:sponsor-cancel",
                kwargs={"story": story, "ref": "stripe_session.payment_intent"},
            )
        ),
        # metadata={
        #     "story": package.story.summary,
        # },
    )
    sponsor = Sponsors.objects.create(
        package=package,
        user=request.user,
        reference=stripe_session.payment_intent,
        status="pending",
    )
    sponsor.save()
    return HttpResponseRedirect(stripe_session.url)


def sponsor_success(request, story, ref):
    verify = stripe.PaymentIntent.retrieve(ref)

    # Extract the necessary information from the payment intent object
    amount = verify["amount"]
    currency = verify["currency"]
    payment_status = verify["status"]
    sponsor = Sponsors.objects.get(reference=ref)
    sponsor.status = "succeeded"
    sponsor.payment_date = timezone.now()
    sponsor.expire_at = sponsor.payment_date + timezone.timedelta(days=30)
    sponsor.save()
    context = {
        "sponsor": sponsor,
        "status": payment_status,
    }
    return render(request, "sponsorship/sponsor-success.html", context)


def sponsor_cancel(request, story, ref):
    return render(request, "sponsorship/sponsor-cancel.html")
