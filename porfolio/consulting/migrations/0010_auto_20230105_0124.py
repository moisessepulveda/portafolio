# Generated by Django 3.2.16 on 2023-01-05 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0009_formfield_formpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='formpage',
            name='form_button_text',
            field=models.CharField(default='Enviar', max_length=50, verbose_name='Texto del botón'),
        ),
        migrations.AddField(
            model_name='formpage',
            name='form_title',
            field=models.CharField(max_length=50, null=True, verbose_name='Título del formulario'),
        ),
        migrations.AlterField(
            model_name='formpage',
            name='description',
            field=models.TextField(verbose_name='Descripción'),
        ),
    ]