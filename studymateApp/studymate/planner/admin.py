from django.contrib import admin

from .models import Todo, Schedule, Comment
# Register your models here.

admin.site.register(Todo)
admin.site.register(Schedule)
admin.site.register(Comment)