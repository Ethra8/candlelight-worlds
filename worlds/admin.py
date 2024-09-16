from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import World

# Register your models here.

@admin.register(World)
class WorldAdmin(SummernoteModelAdmin):
    list_display = ('id', 'slug', 'display_name', 'description', 'image', 'image_dining', 'image_jakuzzi',)
    prepopulated_fields = {'slug': ('display_name',)}
    summernote_fields = ('description',)