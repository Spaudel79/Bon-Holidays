# Generated by Django 3.0.8 on 2020-10-09 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(default='hello@hello.com', max_length=254)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]