# Generated by Django 2.2 on 2021-07-11 09:33

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("packages", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Test",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("new", ckeditor.fields.RichTextField()),
                (
                    "package",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="test",
                        to="packages.Package",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomBooking",
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
                ("contacted", models.BooleanField(default=False)),
                (
                    "people",
                    models.CharField(
                        choices=[
                            ("Single", "Single"),
                            ("Couple", "Couple"),
                            ("Family", "Family"),
                            ("Group", "Group"),
                        ],
                        default="Couple",
                        max_length=64,
                    ),
                ),
                ("number_of_children", models.IntegerField(default=0)),
                ("number_of_adults", models.IntegerField(default=0)),
                ("country", models.CharField(max_length=255)),
                ("bookedfor", models.DateField(blank=True, null=True)),
                (
                    "age_group",
                    models.CharField(
                        choices=[
                            ("18-35 yrs", "18-35 yrs"),
                            ("36-50 yrs", "36-50 yrs"),
                            ("51-64 yrs", "51-64 yrs"),
                            ("65+ yrs", "65+ yrs"),
                        ],
                        default="18-35 yrs",
                        max_length=64,
                    ),
                ),
                (
                    "tour_type",
                    models.CharField(
                        choices=[
                            (
                                "Custom-made trip with guide and/or driver",
                                "Custom-made trip with guide and/or driver",
                            ),
                            (
                                "Custom-made trip without guide and driver",
                                "Custom-made trip without guide and driver",
                            ),
                            ("Group Tour", "Group Tour"),
                            ("Cruise Tour", "Cruise Tour"),
                        ],
                        default="Group Tour",
                        max_length=100,
                    ),
                ),
                (
                    "accomodation",
                    models.CharField(
                        choices=[
                            ("Basic", "Basic"),
                            ("Comfortable", "Comfortable"),
                            ("Luxury", "Luxury"),
                            ("Quirky", "Quirky"),
                        ],
                        default="Quirky",
                        max_length=100,
                    ),
                ),
                ("budget", models.FloatField(blank=True)),
                (
                    "trip_stage",
                    models.CharField(
                        choices=[
                            (
                                "I need more information before I can start trip planning",
                                "I need more information before I can start trip planning",
                            ),
                            (
                                "I'm ready to start trip planning",
                                "I'm ready to start trip planning",
                            ),
                            (
                                "I've done my homework and almost ready to book",
                                "I've done my homework and almost ready to book",
                            ),
                        ],
                        default="I'm ready to start trip planning",
                        max_length=255,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("created_at",),
            },
        ),
        migrations.CreateModel(
            name="Booking",
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
                ("contacted", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=255)),
                ("bookedfor", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "package",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="package",
                        to="packages.Package",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("created_at",),
            },
        ),
    ]
