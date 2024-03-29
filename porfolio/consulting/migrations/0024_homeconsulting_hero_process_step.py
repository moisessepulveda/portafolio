# Generated by Django 3.2.16 on 2023-01-05 03:54

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0023_auto_20230105_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeconsulting',
            name='hero_process_step',
            field=wagtail.fields.StreamField([('card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='imagen')), ('title', wagtail.blocks.TextBlock(label='titulo')), ('subtitle', wagtail.blocks.TextBlock(label='subtitulo')), ('description', wagtail.blocks.RichTextBlock(label='descripcion'))]))], null=True, use_json_field=None),
        ),
    ]
