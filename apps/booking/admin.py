from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.contrib.admin import ModelAdmin, register

# Register your models here.

@register(Booking)
class BookingAdmin(ModelAdmin):

    # autocomplete_fields = ['author']
    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/booking/booking/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/booking/booking/{}/delete/">Delete</a>', obj.id)

    list_display = ('user', 'package', 'name', 'email', 'phone', 'bookedfor', 'created_at', 'edit', 'delete')
    icon_name = 'assignment'


@register(Test)
class TestAdmin(ModelAdmin):

    # autocomplete_fields = ['author']
    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/booking/test/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/booking/test/{}/delete/">Delete</a>', obj.id)

    list_display = ('email', 'name', 'edit', 'delete')
    icon_name = 'assignment'



@register(CustomBooking)
class CustomBookingAdmin(ModelAdmin):

    # autocomplete_fields = ['author']
    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/booking/custombooking/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/booking/custombooking/{}/delete/">Delete</a>', obj.id)

    list_display = ('user', 'people', 'number_of_children', 'number_of_adults',
                    'age_group', 'tour_type', 'accomodation', 'budget',  'Trip_stage',
                     'trip_title', 'bookedfor', 'created_at', 'edit', 'delete')
    icon_name = 'assignment'
