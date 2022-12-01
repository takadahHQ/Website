from django.utils.functional import SimpleLazyObject
import time
from .utils import getUserAgents
from modules.stats.tasks import ingress_request
from ipware import get_client_ip

def ingress(request, service_uuid, identifier, tracker, payload):
    time = time.timezone.now()
    client_ip, is_routable = get_client_ip(request)
    location = request.META.get("HTTP_REFERER", "").strip()
    user_agent = request.META.get("HTTP_USER_AGENT", "").strip()
    dnt = request.META.get("HTTP_DNT", "0").strip() == "1"
    gpc = request.META.get("HTTP_SEC_GPC", "0").strip() == "1"
    if gpc or dnt:
        dnt = True

    ingress_request.delay(
        service_uuid,
        tracker,
        time,
        payload,
        client_ip,
        location,
        user_agent,
        dnt=dnt,
        identifier=identifier,
    )


class UserAgentMiddleware(object):
    def __init__(self, get_response=None):
        if get_response is not None:
            self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        return self.get_response(request)

    def process_request(self, request):
        request.user_agent = SimpleLazyObject(lambda: getUserAgent(request))


class AnalyticsMiddleware(object):
    def process_request(self, request, **args, **kwargs):
        self.start_time = time.time()
        payload = json.loads(self.request.body)
        # hit, hit_created = HitCount.objects.get_or_create(url=request.path)
        # hit.hits = F('hits') + 1
        # hit.save()
        ingress(
            self.request,
            self.kwargs.get("service_uuid"),
            self.kwargs.get("identifier", ""),
            "BACK",
            payload,
        )
        return response

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response

    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse("index"):
            return None

        start = time.time()
        response = func(request)
        costed = time.time() - start
        print("process view: {:.2f}s".format(costed))
        return response

    def process_response(self, request, response):
        costed = time.time() - self.start_time
        return response
