# Generated by Django 3.2.16 on 2023-01-13 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0028_auto_20230106_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeconsulting',
            name='hero_team',
            field=models.CharField(default='', max_length=100, verbose_name='titulo nuestro equipo'),
        ),
        migrations.AddField(
            model_name='homeconsulting',
            name='hero_team_title',
            field=models.CharField(default='', max_length=100, verbose_name='nuestro equipo descripción'),
        ),
    ]
