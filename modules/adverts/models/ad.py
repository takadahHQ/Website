from django.db import models
from modules.adverts.models.include import statusModel, AdManager
from django.urls import reverse
from django.utils import timezone


def now_plus_1_day():
    return timezone.now() + timezone.timedelta(days=1)


class Ad(statusModel):
    """
    This is our base model, from which all ads will inherit.
    The manager methods for this model will determine which ads to
    display return etc.
    """

    title = models.CharField(verbose_name="Title", max_length=255)
    description = models.TextField(verbose_name="Description", blank=True)
    url = models.URLField(verbose_name="Advertised URL")

    publication_date = models.DateTimeField(
        verbose_name="Start showing", auto_now_add=True
    )
    publication_date_end = models.DateTimeField(
        verbose_name="Stop showing", default=now_plus_1_day
    )

    # Relations
    advertiser = models.ForeignKey(
        "Advertiser", on_delete=models.CASCADE, verbose_name="Ad Provider"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        verbose_name="Category",
        blank=True,
        null=True,
    )
    zone = models.CharField(verbose_name="Zone", max_length=100)
    weight = models.IntegerField(
        verbose_name="Weight",
        help_text="Weight of the ad relative to other ads "
        "in the same zone.<br/>"
        "Ad with higher weight will be "
        "displayed more frequently.",
        default=1,
        # validators=[MinValueValidator(1)],
    )
    target_blank = models.BooleanField(verbose_name="Open in new tab", default=False)
    price = models.DecimalField(
        verbose_name="Price", max_digits=10, decimal_places=2, default=0.00
    )
    objects = AdManager()

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ads:ad-click", kwargs={"pk": self.id})

    def calculate_weight(self):
        """
        Calculates the weight of the ad based on its price compared to the average
        price of active ads in the same zone.
        """
        active_ads = Ad.objects.filter(
            zone=self.zone,
            publication_date__lte=timezone.now(),
            publication_date_end__gte=timezone.now(),
        )
        avg_price = active_ads.aggregate(Avg("price"))["price__avg"]
        if avg_price is None:
            avg_price = 0
        if self.price > avg_price:
            return int(self.price / avg_price)
        else:
            return 1

    def update_weight(self):
        now = timezone.now()
        publication_date = self.publication_date
        publication_date_end = self.publication_date_end

        if not publication_date or publication_date > now:
            return 0

        if publication_date_end and publication_date_end < now:
            return 0

        total_weight = self.weight

        # Get all the clicks for the ad in the last 30 days
        thirty_days_ago = now - datetime.timedelta(days=30)
        ad_clicks = Click.objects.filter(ad=self, clicked_at__gte=thirty_days_ago)

        # Calculate the total number of clicks for the ad in the last 30 days
        total_clicks = (
            ad_clicks.aggregate(total_clicks=Count("id"))["total_clicks"] or 0
        )

        # Calculate the average clicks per day for the ad in the last 30 days
        days_since_publication = (now - publication_date).days + 1
        if days_since_publication < 30:
            avg_clicks_per_day = total_clicks / days_since_publication
        else:
            avg_clicks_per_day = total_clicks / 30

        # Adjust the total weight based on the average clicks per day
        if avg_clicks_per_day:
            weight_adjustment = avg_clicks_per_day / self.clicks_per_day
            total_weight = round(total_weight * weight_adjustment)

        return total_weight

    def save(self, *args, **kwargs):
        self.weight = self.calculate_weight()
        super().save(*args, **kwargs)

    def get_impression_count(self):
        """
        Returns the total number of impressions for this ad.
        """
        return self.impressions.count()

    def get_click_count(self):
        """
        Returns the total number of clicks for this ad.
        """
        return self.clicks.count()

    def get_impression_rate(self):
        """
        Returns the impression rate for this ad, calculated as the
        percentage of impressions that resulted in a click.
        """
        impression_count = self.get_impression_count()
        click_count = self.get_click_count()
        if impression_count == 0:
            return 0
        else:
            return click_count / impression_count * 100

    def get_total_impressions(self):
        """
        Returns the total number of impressions for this ad and all other ads
        in the same zone that have ended.
        """
        impressions = Impression.objects.filter(
            ad__zone=self.zone,
            ad__publication_date_end__lt=timezone.now(),
        )
        return impressions.count()

    def get_total_clicks(self):
        """
        Returns the total number of clicks for this ad and all other ads
        in the same zone that have ended.
        """
        clicks = Click.objects.filter(
            ad__zone=self.zone,
            ad__publication_date_end__lt=timezone.now(),
        )
        return clicks.count()
