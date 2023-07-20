import random
import string
from django.urls import reverse
from django.utils.functional import SimpleLazyObject
from modules.stats.utils import getUserAgent
from modules.stats.tasks import ingress_request
from ipware import get_client_ip
from django.utils import timezone


def generate_idempotency():
    random_chars = string.ascii_letters + string.digits
    return "".join(random.choice(random_chars) for _ in range(30))


class AnalyticsMiddleware:
    def __init__(self, get_response=None):
        if get_response is not None:
            self.get_response = get_response

    def __call__(self, request):
        # Record the start time before processing the request
        start_time = timezone.now()

        # Process the request and get the response
        response = self.get_response(request)

        # Record the end time after processing the request
        end_time = timezone.now()
        # Calculate the page load time in seconds
        page_load_time = end_time - start_time

        if request.method == "GET":
            # The details to fill the ingress
            location = request.META.get("HTTP_REFERER", "").strip()
            current_page_url = request.build_absolute_uri()
            service = "de0dc5ca-e70d-480a-82db-003bb4f42992"
            tracker = "BACK"
            time = timezone.now()
            client_ip, is_routable = get_client_ip(request)
            current_page_url = request.build_absolute_uri()
            location = request.META.get("HTTP_REFERER", "").strip()
            user_agent = request.META.get("HTTP_USER_AGENT", "").strip()
            dnt = request.META.get("HTTP_DNT", "0").strip() == "1"
            gpc = request.META.get("HTTP_SEC_GPC", "0").strip() == "1"
            identifier = ""
            if request.resolver_match is not None:
                identifier = request.resolver_match.kwargs.get("identifier", "")

            # Generate idempotency for this request and session
            idempotency = generate_idempotency()

            payload = {
                "idempotency": idempotency,
                "location": current_page_url,
                "referer": location,
                "loadTime": page_load_time.total_seconds(),
            }

            # Send analytics data to the server
            ingress_request(
                service_uuid=service,
                tracker=tracker,
                time=time,
                payload=payload,
                ip=client_ip,
                location=location,
                user_agent=user_agent,
                dnt=dnt,
                identifier=identifier,
            )

        return response
