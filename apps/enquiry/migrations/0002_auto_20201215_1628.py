# Generated by Django 3.0.8 on 2020-12-15 10:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, default=-1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactform',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, default=-1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=ckeditor.fields.RichTextField(blank=True, default=-1),
            preserve_default=False,
        ),
    ]
