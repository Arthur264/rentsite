from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import UserProfile
# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 1
    can_delete = False
    fk_name = 'user'
  
class CustomUser(UserAdmin):
    inlines = (UserProfileInline,)
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUser, self).get_inline_instances(request, obj)

    
admin.site.unregister(User)
admin.site.register(User, CustomUser)