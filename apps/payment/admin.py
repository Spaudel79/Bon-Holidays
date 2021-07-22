from django.contrib import admin
from .models import Payment
from django.contrib.admin import ModelAdmin, register

# Register your models here.

@register(Payment)
class PaymentAdmin(ModelAdmin):
    list_display = ('name',)
    icon_name = 'attach_money'