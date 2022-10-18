from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'email_id', 'subject')
admin.site.register(Category, CategoryAdmin)