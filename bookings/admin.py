
from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('date', 'world','start_time', 'user', 'id',)

admin.site.register(Booking, BookingAdmin)