# Generated by Django 3.2.16 on 2023-01-05 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0020_auto_20230105_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeconsulting',
            name='hero_services_desc',
            field=models.CharField(default='servicios descripcion', max_length=200, verbose_name='servicios descripcion'),
        ),
        migrations.AddField(
            model_name='homeconsulting',
            name='hero_services_title',
            field=models.CharField(default='servicios titulo', max_length=100, verbose_name='servicios titulo'),
        ),
    ]
