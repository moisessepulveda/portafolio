# Generated by Django 3.2.13 on 2022-06-12 20:14

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('simplelist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('content', wagtail.core.fields.RichTextField(verbose_name='Contenido')),
            ],
            options={
                'verbose_name': 'Página de terminos',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='simplelistpage',
            name='description',
        ),
        migrations.AddField(
            model_name='simplelistpage',
            name='app_store_url',
            field=models.URLField(blank=True, null=True, verbose_name='URL App store'),
        ),
        migrations.AddField(
            model_name='simplelistpage',
            name='description_section1',
            field=wagtail.core.fields.RichTextField(default='', verbose_name='Descripción sección 1'),
        ),
        migrations.AddField(
            model_name='simplelistpage',
            name='description_section2',
            field=wagtail.core.fields.RichTextField(default='', verbose_name='Descripción sección 2'),
        ),
        migrations.AddField(
            model_name='simplelistpage',
            name='description_section3',
            field=wagtail.core.fields.RichTextField(default='', verbose_name='Descripción sección 3'),
        ),
        migrations.AddField(
            model_name='simplelistpage',
            name='download_caption',
            field=models.CharField(blank=True, default='', max_length=80, null=True, verbose_name='Descripción descarga'),
        ),
        migrations.AddField(
            model_name='simplelistpage',
            name='gplay_url',
            field=models.URLField(blank=True, null=True, verbose_name='URL de Google Play'),
        ),
        migrations.AddField(
            model_name='simplelistpage',
            name='hero_changing_words',
            field=models.CharField(default='útil, todo terreno', help_text="Separadas por ','", max_length=100, verbose_name='Secuencia de palabras'),
        ),
        migrations.AddField(
            model_name='simplelistpage',
            name='hero_subtitle',
            field=models.CharField(default='Simple list te permitirá llevar el calculo de tu compra en todo momento', max_length=100, verbose_name='Subtítulo'),
        ),
        migrations.AddField(
            model_name='simplelistpage',
            name='hero_title',
            field=models.CharField(default='Simple list', max_length=50, verbose_name='Título'),
        ),
        migrations.AddField(
            model_name='simplelistpage',
            name='subtitle_section3',
            field=models.CharField(default='', max_length=50, verbose_name='Subtítulo sección 3'),
        ),
        migrations.AddField(
            model_name='simplelistpage',
            name='title_section1',
            field=models.CharField(default='', max_length=50, verbose_name='Titulo sección 1'),
        ),
        migrations.AddField(
            model_name='simplelistpage',
            name='title_section2',
            field=models.CharField(default='', max_length=50, verbose_name='Titulo sección 2'),
        ),
        migrations.AddField(
            model_name='simplelistpage',
            name='title_section3',
            field=models.CharField(default='', max_length=50, verbose_name='Titulo sección 3'),
        ),
        migrations.CreateModel(
            name='FooterSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_title', models.CharField(default='', max_length=20, verbose_name='Título del footer')),
                ('footer_desc', models.TextField(default='', verbose_name='Descripción del footer')),
                ('footer_link_label', models.CharField(default='Enlaces', max_length=20, verbose_name='Etiqueta enlace')),
                ('footer_copyright', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('footer_email', models.EmailField(default='myemail@email.com', max_length=254)),
                ('footer_urls', wagtail.core.fields.StreamField([('url', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(label='Etiqueta', max_length=50)), ('urls', wagtail.core.blocks.URLBlock(label='URL'))], label='URL'))], blank=True, default='', null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Datos del pie de página',
            },
        ),
    ]
