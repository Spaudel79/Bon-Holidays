# Generated by Django 2.2 on 2021-07-11 09:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BecomePartner",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=255, null=True)),
                ("last_name", models.CharField(blank=True, max_length=255, null=True)),
                ("company_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                "verbose_name_plural": "Potential Partners",
            },
        ),
        migrations.CreateModel(
            name="ChooseUs",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=500, null=True)),
                ("description", ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "Why Choose Info",
            },
        ),
        migrations.CreateModel(
            name="Partner",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "pic",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="Banner Image"
                    ),
                ),
                ("description", ckeditor.fields.RichTextField(blank=True, null=True)),
                (
                    "join_title1",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("description_1", ckeditor.fields.RichTextField(blank=True, null=True)),
                (
                    "join_title2",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("description_2", ckeditor.fields.RichTextField(blank=True, null=True)),
                (
                    "join_title3",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("description_3", ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "Partner Info",
            },
        ),
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "native_place",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("pic", models.ImageField(blank=True, null=True, upload_to="")),
                ("description", ckeditor.fields.RichTextField(blank=True, null=True)),
                ("tour_title", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "rating",
                    models.IntegerField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AboutUs",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("welcome_title", models.CharField(blank=True, max_length=500)),
                (
                    "pic",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="Banner Image"
                    ),
                ),
                ("welcome_description", models.TextField(blank=True, null=True)),
                ("welcome_pic", models.ImageField(blank=True, null=True, upload_to="")),
                (
                    "happy_travellers",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "satisfied_tours",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "total_destination",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "choose_info",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        to="office.ChooseUs",
                        verbose_name="Choose Info(Add only three infos)",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "About Us Info",
            },
        ),
    ]
