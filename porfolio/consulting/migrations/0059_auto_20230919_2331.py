# Generated by Django 3.2.16 on 2023-09-19 23:31

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0058_auto_20230919_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeconsulting',
            name='hero_clients_desc',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='que han confiado en nosotros'),
        ),
        migrations.AlterField(
            model_name='homeconsulting',
            name='hero_clients_members',
            field=wagtail.fields.StreamField([('card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Imagen'))]))], null=True, use_json_field=True),
        ),
    ]