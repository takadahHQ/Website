import random
import string
from django.utils.functional import SimpleLazyObject
from modules.stats.utils import getUserAgent
from modules.stats.tasks import ingress_request
from ipware import get_client_ip
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.urls import resolve
from modules.stories.models import Stories


class UserAgentMiddleware:
    def __init__(self, get_response=None):
        if get_response is not None:
            self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        return self.get_response(request)

    def process_request(self, request):
        request.user_agent = SimpleLazyObject(lambda: getUserAgent(request))


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
            tracker = "BACK"
            time = timezone.now()
            identifier, model = self.get_identifier_and_model_from_request(request)
            service = self.get_service_id(identifier, model)
            client_ip, is_routable = get_client_ip(request)
            current_page_url = request.build_absolute_uri()
            location = request.META.get("HTTP_REFERER", "").strip()
            user_agent = request.META.get("HTTP_USER_AGENT", "").strip()
            dnt = request.META.get("HTTP_DNT", "0").strip() == "1"
            gpc = request.META.get("HTTP_SEC_GPC", "0").strip() == "1"
            # identifier = ""
            # if request.resolver_match is not None:
            #     identifier = request.resolver_match.kwargs.get("identifier", "")

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
                service_id=service,
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

    def get_service_id(self, identifier, model):
        try:
            # Get the ContentType for the generic relation
            content_type = ContentType.objects.get_for_model(model)
            stats = model.objects.get(slug=identifier)
            service = stats.service.get(content_type=content_type)
            return service.id
        except ObjectDoesNotExist:
            return (
                "1"  # Handle the case when the service is not found or does not exist
            )

    def get_identifier_from_resolved_match(self, resolved_match):
        view_name = resolved_match.view_name

        if view_name == "stories:show":
            slug = resolved_match.kwargs.get("slug")
            # Use the 'slug' parameter from 'resolved_match.kwargs'
            return slug, Stories

        if view_name == "stories:read":
            # Use the 'slug' parameter from 'resolved_match.kwargs'
            story_slug = resolved_match.kwargs.get("story")
            # chapter_slug = resolved_match.kwargs.get("slug")
            # return chapter_slug
            return story_slug, Stories

        # Add more conditions for other views if needed
        # ...

        # If no match found, return None or handle it accordingly
        return "", Stories

    def get_identifier_and_model_from_request(self, request):
        # Use Django's 'resolve' function to get the resolved match
        resolved_match = resolve(request.path_info)
        return self.get_identifier_from_resolved_match(resolved_match)
