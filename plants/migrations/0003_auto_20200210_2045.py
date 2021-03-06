# Generated by Django 3.0.3 on 2020-02-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_auto_20200210_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', max_length=100, verbose_name='Name slug'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='required_humidity',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=10, verbose_name='Humidity'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='required_temperature',
            field=models.CharField(choices=[('cold', 'Cold'), ('medium', 'Medium'), ('warm', 'Warm')], max_length=10, verbose_name='Temperature'),
        ),
    ]
