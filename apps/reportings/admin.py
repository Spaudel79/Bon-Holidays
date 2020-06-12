from django.contrib import admin
from .models import Report
from django.contrib.admin import ModelAdmin, register

# Register your models here.

@register(Report)
class ReportAdmin(ModelAdmin):
    list_display = ('name',)
    # icon_name = ''
