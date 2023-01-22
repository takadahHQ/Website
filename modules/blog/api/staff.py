from ninja import Router

router = Router()


@router.get("/staff")
def hello(request):
    return "Hello staff"
