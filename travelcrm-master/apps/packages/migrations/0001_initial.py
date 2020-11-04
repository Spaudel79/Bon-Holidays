# Generated by Django 3.0.8 on 2020-11-03 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('dest_image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TopAttractions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='TopActivities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=255)),
                ('featured', models.BooleanField(default=False)),
                ('price', models.IntegerField()),
                ('duration', models.IntegerField(default=5)),
                ('discount', models.CharField(default='15% OFF', max_length=255)),
                ('discounted_price', models.IntegerField(default=230)),
                ('savings', models.IntegerField(default=230)),
                ('special_discout', models.BooleanField(default=False)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('content', models.CharField(max_length=255)),
                ('highlights', models.CharField(max_length=255)),
                ('itinerary', models.CharField(max_length=255)),
                ('reviews', models.CharField(max_length=255)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_created', models.DateField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.Destination')),
            ],
        ),
    ]
