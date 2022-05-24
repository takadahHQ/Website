from django.contrib import admin
from .models import Users, Menus, Transactions, Transfers, Wallets, Settings, Socials, Languages, Kycs, KycDocuments
# Register your models here.

admin.site.register(Users)
admin.site.register(Menus)
admin.site.register(Transactions)
admin.site.register(Transfers)
admin.site.register(Wallets)
admin.site.register(Settings)
admin.site.register(Socials)
admin.site.register(Languages)
admin.site.register(Kycs)
admin.site.register(KycDocuments)
