# Generated by Django 3.0.2 on 2020-02-16 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entry',
            new_name='Topping',
        ),
    ]
