from modules.core.models import Menus, Settings, Socials


def settings(request):
    settings = Settings.objects.filter(status="active").first()
    return {"settings": settings}


def socials(request):
    socials = Socials.objects.filter(status="active").order_by("name")[:10]
    return {"socials": socials}


def menus(request):
    socials = Menus.objects.filter(status="active").order_by("name")[:10]
    return {"menus": socials}
