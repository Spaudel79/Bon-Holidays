# Generated by Django 2.2 on 2021-04-18 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0003_auto_20210307_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='phone',
            field=models.CharField(default=-1, max_length=255),
            preserve_default=False,
        ),
    ]
