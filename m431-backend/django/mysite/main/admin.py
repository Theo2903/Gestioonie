from django.contrib import admin
from main.models import Observation, Appreciation

# Register your models here.
class ObservationAdmin(admin.ModelAdmin):
    list_display = ('key', 'title')
    search_fields = ('key',)

class AppreciationAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_observation_title', 'date_time')
    search_fields = ('user__first_name',)
    list_filter = ('appreciation__title',)

    def get_observation_title(self, obj):
        return obj.appreciation.title


admin.site.register(Observation, ObservationAdmin)

admin.site.register(Appreciation, AppreciationAdmin)