# Generated by Django 3.0.8 on 2020-12-18 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20201218_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='Admin', max_length=64),
        ),
    ]
