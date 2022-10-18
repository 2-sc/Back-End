from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'nickname', 'image', 'info','d_day_start', 'd_day_end', 'd_day']
admin.site.register(User, UserAdmin)
