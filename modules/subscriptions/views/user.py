from datetime import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from modules.subscriptions.models import Sponsors, Packages
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from dotenv import load_dotenv
import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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


@login_required
def sponsor(request, story, slug):
    package = Packages.objects.get(slug=slug)

    stripe.api_key = os.environ.get("STRIPE_KEY")
    sponsor = Sponsors.objects.create(
        package=package,
        user=request.user,
        status="pending",
    )
    sponsor.save()
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
                    "ref": sponsor.id,
                },
            )
        ),
        cancel_url=request.build_absolute_uri(
            reverse(
                "sponsor:sponsor-cancel",
                kwargs={"ref": sponsor.id},
            )
        ),
    )
    sponsor = sponsor
    sponsor.reference = stripe_session.id
    sponsor.save()
    return HttpResponseRedirect(stripe_session.url)


@login_required
def sponsor_success(request, ref):
    sponsor = get_object_or_404(Sponsors, id=ref, user=request.user)

    # intent_id = session.payment_intent
    # print(intent_id)
    # intent = stripe.PaymentIntent.retrieve(intent_id)
    try:
        # Extract the necessary information from the payment intent object
        session = stripe.checkout.Session.retrieve(sponsor.reference)
        if session.payment_status == "paid":
            subscription = stripe.Subscription.retrieve(session.subscription)

            # Verify the subscription
            if subscription.status == "active":
                sponsor.status = "succeeded"
                sponsor.payment_date = timezone.now()
                sponsor.expire_at = sponsor.payment_date + timezone.timedelta(days=30)
                sponsor.save()

                messages.success(
                    request,
                    f"Successfully sponsored {sponsor.package.story.title}. Thank you for your support!",
                )
                context = {
                    "sponsor": sponsor,
                }
                return render(request, "sponsorship/sponsor-success.html", context)

            else:
                # Subscription is not active, cancel the payment
                stripe.PaymentIntent.cancel(session.payment_intent)
                sponsor.delete()

    except stripe.error.InvalidRequestError:
        pass
    raise Http404()


@login_required
def sponsor_cancel(request, ref):
    sponsor = get_object_or_404(Sponsors, id=ref, user=request.user)
    # Extract the necessary information from the payment intent object
    intent = stripe.checkout.Session.retrieve(sponsor.reference)
    intent.cancel()
    sponsor.delete()
    return render(request, "sponsorship/sponsor-cancel.html")
