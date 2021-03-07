from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django import forms


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = (
            'operator','destination', 'package_name', 'duration',
            'featured', 'price', 'discount', 'discounted_price',
            'image', 'itinerary_text', 'content',
            'highlights', 'inclusions', 'exclusions',
            'city', 'tour_type','new_activity', 'accommodation',
            'transport', 'age_range','savings', 'fix_departure',
            'rating',  'image_1', 'image_2', 'image_3',
            'date_created',
        )