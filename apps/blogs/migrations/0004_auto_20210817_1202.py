# Generated by Django 2.2 on 2021-08-17 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blogpost_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blogpost', to='packages.Destination'),
        ),
    ]
