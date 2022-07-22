
from ninja import NinjaAPI

api = NinjaAPI(version='0.0.1')


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}

@api.get("/hello")
def hello(request):
    return "Hello Netesy"