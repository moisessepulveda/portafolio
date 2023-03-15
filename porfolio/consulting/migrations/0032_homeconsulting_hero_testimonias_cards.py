# Generated by Django 3.2.16 on 2023-01-22 15:58

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0031_auto_20230114_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeconsulting',
            name='hero_testimonias_cards',
            field=wagtail.fields.StreamField([('card', wagtail.blocks.StructBlock([('name', wagtail.blocks.TextBlock(label='nombre')), ('position', wagtail.blocks.TextBlock(label='cargo')), ('description', wagtail.blocks.RichTextBlock(label='descripcion'))]))], null=True, use_json_field=True),
        ),
    ]
