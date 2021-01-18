# Generated by Django 3.0.8 on 2021-01-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0003_auto_20210115_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='package',
            name='new_activity',
        ),
        migrations.AddField(
            model_name='package',
            name='new_activity',
            field=models.ManyToManyField(to='packages.NewActivity'),
        ),
    ]