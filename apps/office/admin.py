from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin, register

# Register your models here.


@register(ChooseUs)
class ChooseUsAdmin(ModelAdmin):
    icon_name = "pan_tool"


# class ChooseUsAdmin(admin.TabularInline):
#     model = ChooseUs

# @register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("welcome_title", "happy_travellers", "total_destination")
    icon_name = "portrait"
    # inlines = [ChooseUsAdmin]


@register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "tour_title",
        "rating",
    )
    icon_name = "markunread"


@register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("title",)
    icon_name = "person_pin"


@register(BecomePartner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "company_name",
        "email",
        "phone",
    )
    icon_name = "person_add"


admin.site.register(AboutUs, AboutUsAdmin)
