# Generated by Django 3.2.16 on 2022-12-23 23:33

from django.db import migrations, models
import django.db.models.deletion
import home.models
import modelcluster.fields
import wagtail.blocks
import wagtail.contrib.forms.models
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
        ('wagtailimages', '0024_index_image_file_hash'),
        ('wagtaildocs', '0012_uploadeddocument'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, validators=[wagtail.contrib.forms.models.validate_to_address], verbose_name='to address')),
                ('from_address', models.EmailField(blank=True, max_length=255, verbose_name='from address')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Nombre')),
                ('profession', models.CharField(max_length=100, null=True, verbose_name='Profesión')),
                ('age', models.IntegerField(default=18, verbose_name='Edad')),
                ('phone', models.CharField(max_length=100, null=True, verbose_name='Teléfono')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Correo electrónico')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='Dirección')),
                ('github_link', models.URLField(blank=True, null=True, verbose_name='Enlace de github')),
                ('linkedin_link', models.URLField(blank=True, null=True, verbose_name='Enlace linked IN')),
                ('facebook_link', models.URLField(blank=True, null=True, verbose_name='Enlace de facebook')),
                ('youtube_link', models.URLField(blank=True, null=True, verbose_name='Enlace de YouTube')),
                ('presentation_title', models.CharField(max_length=50, null=True, verbose_name='Título')),
                ('presentation_desc', models.TextField(null=True, verbose_name='Descripción')),
                ('resume_title', models.CharField(default='', max_length=50, verbose_name='Título')),
                ('resume_body', wagtail.fields.RichTextField(null=True, verbose_name='Cuerpo')),
                ('education', wagtail.fields.StreamField([('item', wagtail.blocks.StructBlock([('university', wagtail.blocks.CharBlock(label='Universidad/Instituto')), ('period', wagtail.blocks.CharBlock(label='Periodo')), ('title', wagtail.blocks.RichTextBlock(label='Descripción'))]))], use_json_field=None)),
                ('job_history', wagtail.fields.StreamField([('trabajo', wagtail.blocks.StructBlock([('enterprise', wagtail.blocks.CharBlock(label='Empresa')), ('period', wagtail.blocks.CharBlock(label='Periodo')), ('description', wagtail.blocks.RichTextBlock(label='Descripción'))]))], use_json_field=None)),
                ('skills', wagtail.fields.StreamField([('habilidades', wagtail.blocks.StructBlock([('technology', wagtail.blocks.CharBlock(label='Tecnología')), ('percentage', wagtail.blocks.CharBlock(label='Porcentaje'))]))], use_json_field=None)),
                ('project_title', models.CharField(default='Mis Proyectos_', max_length=50, verbose_name='Titulo')),
                ('projects', wagtail.fields.StreamField([('project', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Título')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Imagen')), ('summary', wagtail.blocks.TextBlock(label='Resumen')), ('descripcion', wagtail.blocks.RichTextBlock(label='Descripción')), ('stack_used', wagtail.blocks.TextBlock(label='Tecnologías utilizadas'))]))], use_json_field=None)),
                ('courses_title', models.CharField(default='Cursos creados por mi_', max_length=50)),
                ('courses_message', wagtail.fields.RichTextField(default='', verbose_name='Mensaje')),
                ('courses', wagtail.fields.StreamField([('curso', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Título')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Imagen')), ('summary', wagtail.blocks.TextBlock(label='Resumen')), ('technology', wagtail.blocks.CharBlock(label='Tecnología')), ('link', wagtail.blocks.URLBlock(label='Enlace Video/Lista'))]))], use_json_field=None)),
                ('testimonials', wagtail.fields.StreamField([('testimonio', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Título')), ('project', wagtail.blocks.CharBlock(label='Proyecto')), ('message', wagtail.blocks.TextBlock(label='Mensaje'))]))], use_json_field=None)),
                ('cv_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document', verbose_name='Archivo de curriculum')),
                ('hero_picture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto')),
            ],
            options={
                'abstract': False,
            },
            bases=(home.models.CustomEmailForm, wagtail.contrib.forms.models.FormMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('clean_name', models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name')),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma or new line separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.TextField(blank=True, help_text='Default value. Comma or new line separated values supported for checkboxes.', verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
