# Generated by Django 3.2.16 on 2023-03-28 00:14

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0038_auto_20230328_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalinfo',
            name='contact_phone',
            field=models.CharField(max_length=100, verbose_name='Teléfono de contacto'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='enterprise_name',
            field=models.CharField(max_length=100, verbose_name='Nombre de la empresa'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='footer_urls',
            field=wagtail.fields.StreamField([('url', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(label='Etiqueta', max_length=50)), ('urls', wagtail.blocks.PageChooserBlock(label='URL'))], label='Enlace'))], blank=True, default='', null=True, use_json_field=True, verbose_name='Enlaces al pie de página'),
        ),
    ]
