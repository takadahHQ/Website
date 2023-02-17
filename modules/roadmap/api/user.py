from ninja import Router

router = Router()


@router.get("/user")
def hello(request):
    return "Hello user"
