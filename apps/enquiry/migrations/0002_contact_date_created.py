# Generated by Django 2.2 on 2021-03-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]