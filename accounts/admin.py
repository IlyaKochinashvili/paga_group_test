from django.contrib import admin

from accounts.models import Account, Profile


@admin.register(Account)
class AccountsAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
