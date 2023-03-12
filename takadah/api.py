from ninja import NinjaAPI

# # accounts
# from modules.accounts.api.user import router as accounts_user_router
# from modules.accounts.api.staff import router as accounts_staff_router

# # core
# from modules.core.api.user import router as core_user_router
# from modules.core.api.staff import router as core_staff_router

# blog
from modules.blog.api.user import router as blog_user_router
from modules.blog.api.staff import router as blog_staff_router

api = NinjaAPI(
    title="Takadah API",
    version="1.0.1",
    description="The API for Takadah",
)
# # accounts
# api.add_router("/account/", accounts_user_router)
# api.add_router("/account/", accounts_staff_router)
# # core
# api.add_router("/core/", core_user_router)
# api.add_router("/core/", core_staff_router)
# # blog
api.add_router("/blog/", blog_user_router)
api.add_router("/blog/", blog_staff_router)
