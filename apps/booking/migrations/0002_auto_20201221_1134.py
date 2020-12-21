# Generated by Django 3.0.8 on 2020-12-21 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='custombooking',
            old_name='Trip_stage',
            new_name='trip_stage',
        ),
        migrations.RemoveField(
            model_name='custombooking',
            name='budget_flexibility',
        ),
        migrations.RemoveField(
            model_name='custombooking',
            name='description',
        ),
        migrations.RemoveField(
            model_name='custombooking',
            name='trip_title',
        ),
        migrations.AddField(
            model_name='custombooking',
            name='country',
            field=models.CharField(default=-1, max_length=255),
            preserve_default=False,
        ),
    ]