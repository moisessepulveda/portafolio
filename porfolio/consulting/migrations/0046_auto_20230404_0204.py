# Generated by Django 3.2.16 on 2023-04-04 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0045_auto_20230404_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalinfo',
            name='whatsapp_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Número de Whatsapp'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='whatsapp_text',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Texto whatsapp'),
        ),
    ]