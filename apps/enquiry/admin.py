from django.contrib import admin
from .models import Contact, Feedback, ContactForm, AddressInfo
from django.contrib.admin import ModelAdmin, register

# Register your models here.


@register(AddressInfo)
class AddressInfoAdmin(ModelAdmin):
    icon_name = "add_location"


@register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = (
        "date_created",
        "phone",
        "email",
    )
    icon_name = "call"


@register(ContactForm)
class ContactFormAdmin(ModelAdmin):
    list_display = (
        "subject",
        "contacted",
        "full_name",
        "email",
    )
    icon_name = "call_end"


@register(Feedback)
class FeedbackAdmin(ModelAdmin):
    list_display = (
        "name",
        "email",
        "contacted",
        "subject",
    )
    icon_name = "feedback"
