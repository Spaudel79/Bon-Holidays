# Generated by Django 3.0.8 on 2020-10-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0005_topattractions'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
