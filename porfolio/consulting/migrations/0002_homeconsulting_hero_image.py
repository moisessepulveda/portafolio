# Generated by Django 3.2.16 on 2022-12-28 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('consulting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeconsulting',
            name='hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen principal'),
        ),
    ]
