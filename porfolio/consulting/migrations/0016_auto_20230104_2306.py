# Generated by Django 3.2.16 on 2023-01-05 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0015_auto_20230104_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeconsulting',
            name='hero_agile_develop_desc',
            field=models.CharField(default='item 1.1', max_length=150, verbose_name='item descripción 1.1'),
        ),
        migrations.AlterField(
            model_name='homeconsulting',
            name='hero_information_security_desc',
            field=models.CharField(default='item 2.1', max_length=150, verbose_name='item descripción 2.1'),
        ),
        migrations.AlterField(
            model_name='homeconsulting',
            name='hero_scalability_desc',
            field=models.CharField(default='item 3.1', max_length=150, verbose_name='item descripción 3.1'),
        ),
    ]