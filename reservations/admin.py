from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('date', 'start_time', 'name', 'num_people', 'phone', 'email', 'notes', 'user')
    list_filter = ('date', 'start_time')
    ordering = ('date', 'start_time')

admin.site.register(Booking, BookingAdmin)
