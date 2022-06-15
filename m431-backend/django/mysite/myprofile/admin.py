from django.contrib import admin

from myprofile.models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('id','user')

# Add UserProfile to User in Django Admin
# Src: https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html
class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    list_display = ('username', 'last_name', 'first_name', 'email')


    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(UserProfile, UserProfileAdmin)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

