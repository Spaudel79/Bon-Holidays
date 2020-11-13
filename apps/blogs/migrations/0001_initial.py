# Generated by Django 3.0.8 on 2020-11-12 10:44

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('categories', models.CharField(choices=[('travel_news', 'Travel News'), ('travel_tips', 'Travel Tips'), ('things_to_do', 'Things to Do'), ('places_to_go', 'Places to Go')], default='travel_news', max_length=64)),
                ('description', ckeditor.fields.RichTextField()),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('tags', models.CharField(default='#travel', max_length=255)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.BlogPost')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
