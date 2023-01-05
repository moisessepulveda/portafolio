# Generated by Django 3.2.16 on 2023-01-05 01:45

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0010_auto_20230105_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formpage',
            name='description',
            field=wagtail.fields.StreamField([('h1', wagtail.blocks.CharBlock(form_classname='title')), ('h2', wagtail.blocks.CharBlock(form_classname='title')), ('h3', wagtail.blocks.CharBlock(form_classname='title')), ('h4', wagtail.blocks.CharBlock(form_classname='title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('quote', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('youtube_video', wagtail.blocks.URLBlock()), ('gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), icon='image', label='Gallery'))], null=True, use_json_field=True, verbose_name='Descripción del servicio'),
        ),
    ]
