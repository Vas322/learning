# Generated by Django 3.0.2 on 2020-03-05 20:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0002_auto_20200216_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name_plural': 'toppings'},
        ),
        migrations.AddField(
            model_name='pizza',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topping',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topping',
            name='addition',
            field=models.CharField(max_length=200),
        ),
    ]
