# Generated by Django 3.2.16 on 2022-12-29 01:50

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('consulting', '0003_serviceconsultingpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceconsultingpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('quote', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('youtube_video', wagtail.blocks.URLBlock()), ('gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), icon='image', label='Gallery'))], null=True, use_json_field=True, verbose_name='Descripción del servicio'),
        ),
        migrations.AddField(
            model_name='serviceconsultingpage',
            name='hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen principal'),
        ),
        migrations.AddField(
            model_name='serviceconsultingpage',
            name='hero_title',
            field=models.CharField(max_length=50, null=True, verbose_name='Título del servicio'),
        ),
    ]
