from django.contrib import admin
from .models import Users, Menus, Transactions, Transfers, Wallets, Settings, Socials, Languages, Kycs, KycDocuments
from .forms import SettingsForm
from hijack.contrib.admin import HijackUserAdminMixin
# Register your models here.

# @admin.register(Users)
# class Users(HijackUserAdminMixin, admin.ModelAdmin):
#     def get_hijack_user(self, obj):
#         return obj.pk
class UserAdmin(HijackUserAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'bio', 'following_count', 'followers_count')

    list_filter = ['language']
    search_fields = ['pseudonym']

    def get_hijack_user(self, obj):
        return obj

admin.site.register(Users, UserAdmin)
admin.site.register(Menus)
admin.site.register(Transactions)
admin.site.register(Transfers)
admin.site.register(Wallets)
@admin.register(Settings)
class Settings(admin.ModelAdmin):
    form = SettingsForm
admin.site.register(Socials)
admin.site.register(Languages)
admin.site.register(Kycs)
admin.site.register(KycDocuments)
