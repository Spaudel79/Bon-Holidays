# Generated by Django 3.0.8 on 2020-12-06 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20201203_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custombooking',
            name='Trip_stage',
            field=models.CharField(choices=[('I need more information before I can start trip planning', 'I need more information before I can start trip planning'), ('I am ready to start trip planning', 'Iam ready to start trip planning'), ('I have done my homework and almost ready to book', 'I have done my homework and almost ready to book')], default='Iam ready to start trip planning', max_length=255),
        ),
        migrations.AlterField(
            model_name='custombooking',
            name='budget_flexibility',
            field=models.CharField(choices=[('No,this is my maximum budget', 'No,this is my maximum budget'), ('Flexible,I can increase up to 20%,if needed', 'Flexible,I can increase up to 20%,if needed'), ('Very flexible, plan me the best trip possible', 'Very flexible, plan me the best trip possible')], default='I can increase upto 20%', max_length=255),
        ),
    ]
