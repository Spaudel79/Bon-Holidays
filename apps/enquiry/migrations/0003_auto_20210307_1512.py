# Generated by Django 2.2 on 2021-03-07 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0002_contact_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='address',
        ),
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.ManyToManyField(blank=True, null=True, to='enquiry.AddressInfo'),
        ),
    ]
