# Generated by Django 2.2 on 2021-02-25 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0011_auto_20210225_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='discounted_price',
        ),
        migrations.AddField(
            model_name='package',
            name='tour_type',
            field=models.CharField(choices=[('Custom-made trip with guide and/or driver', 'Custom-made trip with guide and/or driver'), ('Custom-made trip without guide and driver', 'Custom-made trip without guide and driver'), ('Group Tour', 'Group Tour'), ('Cruise Tour', 'Cruise Tour')], default='Group Tour', max_length=100),
        ),
    ]
