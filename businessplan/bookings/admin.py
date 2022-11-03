from django.contrib import admin
from .models import Booking


admin.site.register(Booking)

# class PriceInline(admin.TabularInline):
#     model = Price


# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#     inlines = [PriceInline]