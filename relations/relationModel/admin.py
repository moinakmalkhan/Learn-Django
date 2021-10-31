from django.contrib import admin
from .models import Page, Song
# Register your models here.


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'page_cat', 'publish_date', 'user']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["name", "duration", "sing_by"]
