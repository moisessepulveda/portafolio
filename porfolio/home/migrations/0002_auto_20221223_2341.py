# Generated by Django 3.2.16 on 2022-12-23 23:41

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='courses',
            field=wagtail.fields.StreamField([('curso', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Título')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Imagen')), ('summary', wagtail.blocks.TextBlock(label='Resumen')), ('technology', wagtail.blocks.CharBlock(label='Tecnología')), ('link', wagtail.blocks.URLBlock(label='Enlace Video/Lista'))]))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='education',
            field=wagtail.fields.StreamField([('item', wagtail.blocks.StructBlock([('university', wagtail.blocks.CharBlock(label='Universidad/Instituto')), ('period', wagtail.blocks.CharBlock(label='Periodo')), ('title', wagtail.blocks.RichTextBlock(label='Descripción'))]))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='job_history',
            field=wagtail.fields.StreamField([('trabajo', wagtail.blocks.StructBlock([('enterprise', wagtail.blocks.CharBlock(label='Empresa')), ('period', wagtail.blocks.CharBlock(label='Periodo')), ('description', wagtail.blocks.RichTextBlock(label='Descripción'))]))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='projects',
            field=wagtail.fields.StreamField([('project', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Título')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Imagen')), ('summary', wagtail.blocks.TextBlock(label='Resumen')), ('descripcion', wagtail.blocks.RichTextBlock(label='Descripción')), ('stack_used', wagtail.blocks.TextBlock(label='Tecnologías utilizadas'))]))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='skills',
            field=wagtail.fields.StreamField([('habilidades', wagtail.blocks.StructBlock([('technology', wagtail.blocks.CharBlock(label='Tecnología')), ('percentage', wagtail.blocks.CharBlock(label='Porcentaje'))]))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='testimonials',
            field=wagtail.fields.StreamField([('testimonio', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Título')), ('project', wagtail.blocks.CharBlock(label='Proyecto')), ('message', wagtail.blocks.TextBlock(label='Mensaje'))]))], use_json_field=True),
        ),
    ]