# Generated by Django 3.2.16 on 2022-12-29 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0005_alter_serviceconsultingpage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceconsultingpage',
            name='side_block_title',
            field=models.CharField(default='Otros servicios', max_length=30, verbose_name='Título bloque del costado'),
        ),
    ]