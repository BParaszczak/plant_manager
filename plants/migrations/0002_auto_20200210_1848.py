# Generated by Django 3.0.3 on 2020-02-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='fertilizing_interval',
            field=models.PositiveIntegerField(help_text='In seconds', verbose_name='Fertilizing interval'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='last_fertilized',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Last fertilizing timestamp'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='last_watered',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Last watering timestamp'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='watering_interval',
            field=models.PositiveIntegerField(help_text='In seconds', verbose_name='Watering interval'),
        ),
    ]
