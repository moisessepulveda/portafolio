# Generated by Django 3.2.16 on 2023-01-05 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0008_remove_serviceconsultingpage_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeconsulting',
            name='hero_over_title',
            field=models.CharField(default='', max_length=50, verbose_name='texto sobre titulo principal'),
        ),
    ]
