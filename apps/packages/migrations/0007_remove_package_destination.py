# Generated by Django 2.2 on 2021-07-22 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0006_auto_20210722_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='destination',
        ),
    ]
