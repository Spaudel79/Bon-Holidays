from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin, register
# Register your models here.

@register(ChooseUs)
class ChooseUsAdmin(ModelAdmin):
    icon_name = 'feedback'

@register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('welcome_title','happy_travellers','total_destination')
    icon_name = 'feedback'

@register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('full_name','tour_title','rating',)
    icon_name = 'feedback'

@register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('title',)
    icon_name = 'feedback'

@register(BecomePartner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('first_name','company_name','email','phone',)
    icon_name = 'feedback'