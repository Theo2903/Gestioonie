from django.contrib import admin
from crud.models import MyObject

class MyObjectAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(MyObject, MyObjectAdmin)