# Generated by Django 2.2 on 2021-07-26 05:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0007_remove_package_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='short_description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
