from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


class AddProfileLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'профиль'


class UserAdmin(BaseUserAdmin):
    inlines = (AddProfileLine,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
