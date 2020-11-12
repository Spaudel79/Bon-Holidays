# Generated by Django 3.0.8 on 2020-11-12 07:06

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='reviews',
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('review', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='packages.Package')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
