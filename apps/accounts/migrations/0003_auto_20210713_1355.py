# Generated by Django 2.2 on 2021-07-13 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_subscribers"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="subscribers",
            options={"verbose_name_plural": "Newsletter Subscribers"},
        ),
    ]
