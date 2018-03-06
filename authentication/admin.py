from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import UserProfile, Role, UserPhone


# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 0
    max_num = 1
    verbose_name_plural = 'Profile'
    can_delete = False
    fk_name = 'user'


class UserPhoneInline(admin.StackedInline):
    model = UserPhone
    extra = 1
    verbose_name_plural = 'Phone'
    can_delete = False
    fk_name = 'user'


class CustomUser(UserAdmin):
    inlines = (UserProfileInline, UserPhoneInline)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUser, self).get_inline_instances(request, obj)



admin.site.unregister(User)
admin.site.register(User, CustomUser)
