# Generated by Django 3.0.8 on 2020-12-25 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='contacted',
            field=models.BooleanField(default=False),
        ),
    ]
