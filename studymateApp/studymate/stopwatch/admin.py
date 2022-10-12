from django.contrib import admin
from .models import StopWatch

# Register your models here.

class StopWatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'subject', 'startTime', 'endTime', 'totalTime')
admin.site.register(StopWatch, StopWatchAdmin)