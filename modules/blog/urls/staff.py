from django.urls import path
from modules.accounts.views import staff

urls = [
    # dashboard
    path(
        "",
        staff.index,
        name="staff.dashboard",
    ),
    # dashboard
    path(
        "/",
        staff.index,
    ),
    # create
    # view
    # edit
    # update
    # delete
]
