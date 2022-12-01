from modules.core.models import Menus, Settings, Socials


def settings(request):
    setting = Settings.objects.filter(status="active").first()
    return {"settings": setting}


def socials(request):
    social = Socials.objects.filter(status="active").order_by("name")[:10]
    return {"socials": social}


def menus(request):
    menu = Menus.objects.filter(status="active").order_by("name")[:10]
    return {"menus": menu}
