# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations



def make_many_destinations(apps, schema_editor):
    """
        Adds the destination object in Package.destination to the
        many-to-many relationship in Package.destinations
    """
    Package = apps.get_model('packages', 'Package')

    for abc in Package.objects.all():
        abc.destinations.add(abc.destination)

class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0005_auto_20210722_1636'),
    ]

    operations = [
        migrations.RunPython(make_many_destinations),
    ]