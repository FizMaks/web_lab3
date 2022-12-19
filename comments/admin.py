from .models import *
from django.contrib import admin

@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'body', 'date_pub']
    list_display_links = ['body']

