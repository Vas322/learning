# Generated by Django 3.0.2 on 2020-03-05 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0003_auto_20200305_2306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topping',
            old_name='name',
            new_name='pizza',
        ),
    ]
