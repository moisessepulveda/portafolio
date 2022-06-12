# Generated by Django 3.2.13 on 2022-06-11 18:46

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('simplelist', '0006_simplelistpage_title_section1'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplelistpage',
            name='title_description1',
            field=wagtail.core.fields.RichTextField(default=''),
        ),
        migrations.AlterField(
            model_name='simplelistpage',
            name='title_section1',
            field=models.CharField(default='', max_length=50, verbose_name='Titulo sección 1'),
        ),
    ]
