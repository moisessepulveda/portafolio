from django.db import models
from django.shortcuts import redirect
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldPanel, InlinePanel
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, FieldPanel, FieldRowPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from modelcluster.fields import ParentalKey
from django.forms import widgets  # used to find TextArea widget
from django.contrib import messages


class FormField(AbstractFormField):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='form_fields')


class CustomEmailForm:
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        # form = super(AbstractEmailForm, self).get_form(*args, **kwargs)  # use this syntax for Python 2.x
        # iterate through the fields in the generated form
        for name, field in form.fields.items():
            # here we want to adjust the widgets on each field
            # if the field is a TextArea - adjust the rows
            # if isinstance(field.widget, widgets.Textarea):
            #    field.widget.attrs.update({'rows': '5'})
            if any([isinstance(field.widget, widgets.TextInput),
                    isinstance(field.widget, widgets.EmailInput),
                    isinstance(field.widget, widgets.Textarea)]):
                field.widget.attrs.update({'placeholder': field.label})

            # for all fields, get any existing CSS classes and add 'form-control'
            # ensure the 'class' attribute is a string of classes with spaces
            css_classes = field.widget.attrs.get('class', '').split()
            css_classes.append('form-control')
            field.widget.attrs.update({'class': ' '.join(css_classes)})
        return form


class HomePage(CustomEmailForm, AbstractEmailForm):

    def render_landing_page(self, request, form_submission=None, *args, **kwargs):
        messages.success(request, 'Tu mensaje se ha enviado Correctamente, Pronto estaremos en contacto')
        return redirect("/")

    # hero fields
    name = models.CharField("Nombre", max_length=100, null=True)
    profession = models.CharField("Profesión", max_length=100, null=True)
    age = models.IntegerField("Edad", default=18)
    phone = models.CharField("Teléfono", null=True, max_length=100)
    email = models.EmailField("Correo electrónico", null=True)
    address = models.CharField("Dirección", max_length=200, null=True)

    github_link = models.URLField("Enlace de github", null=True, blank=True)
    linkedin_link = models.URLField("Enlace linked IN", null=True, blank=True)
    facebook_link = models.URLField("Enlace de facebook", null=True, blank=True)
    youtube_link = models.URLField("Enlace de YouTube", null=True, blank=True)
    footer_legend = models.CharField("Mensaje del footer", null=True, blank=False,
                                     max_length=200,
                                     default='Moisés Sepúlveda - Sitio construido utilizando DJANGO WAGTAIL')
    tab_text = models.CharField("Texto de la pestaña", null=True, blank=False,
                                     max_length=200,
                                     default='Ingresa el título de la pestaña')

    hero_picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Foto",
        related_name='+'
    )
    # hero fields end

    # presentation fields

    presentation_title = models.CharField("Título", max_length=50, null=True)
    presentation_desc = models.TextField("Descripción", null=True)

    cv_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Archivo de curriculum",
        related_name='+'
    )
    # presentation fields end

    # resume fields
    resume_title = models.CharField("Título", max_length=50, default="")
    resume_body = RichTextField("Cuerpo", null=True)

    education = StreamField([
        ('item', blocks.StructBlock([
            ('university', blocks.CharBlock(label="Universidad/Instituto")),
            ('period', blocks.CharBlock(label="Periodo")),
            ('title', blocks.RichTextBlock(label="Descripción")),
        ])),
    ], use_json_field=True)

    job_history = StreamField([
        ('trabajo', blocks.StructBlock([
            ('enterprise', blocks.CharBlock(label="Empresa")),
            ('period', blocks.CharBlock(label="Periodo")),
            ('description', blocks.RichTextBlock(label="Descripción")),
        ])),
    ], use_json_field=True)

    skills = StreamField([
        ('habilidades', blocks.StructBlock([
            ('technology', blocks.CharBlock(label="Tecnología")),
            ('percentage', blocks.CharBlock(label="Porcentaje")),
        ])),
    ], use_json_field=True)

    # resume fields end

    # proyects fields
    project_title = models.CharField("Titulo", max_length=50, default="Mis Proyectos_")
    projects = StreamField([
        ('project', blocks.StructBlock([
            ('title', blocks.CharBlock(label="Título")),
            ('image', ImageChooserBlock(label="Imagen")),
            ('summary', blocks.TextBlock(label="Resumen")),
            ('descripcion', blocks.RichTextBlock(label="Descripción")),
            ('stack_used', blocks.TextBlock(label="Tecnologías utilizadas")),
        ])),
    ], use_json_field=True)

    courses_title = models.CharField(max_length=50, default="Cursos creados por mi_")
    courses_message = RichTextField("Mensaje", default="")
    courses = StreamField([
        ('curso', blocks.StructBlock([
            ('title', blocks.CharBlock(label="Título")),
            ('image', ImageChooserBlock(label="Imagen")),
            ('summary', blocks.TextBlock(label="Resumen")),
            ('technology', blocks.CharBlock(label="Tecnología")),
            ('link', blocks.URLBlock(label="Enlace Video/Lista")),
        ])),
    ], use_json_field=True)

    testimonials = StreamField([
        ('testimonio', blocks.StructBlock([
            ('title', blocks.CharBlock(label="Título")),
            ('project', blocks.CharBlock(label="Proyecto")),
            ('message', blocks.TextBlock(label="Mensaje")),
        ])),
    ], use_json_field=True)

    # proyects field end

    # content panels

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('name', classname="title"),

            FieldRowPanel([
                FieldPanel('profession', classname="full"),
                FieldPanel('age', classname="full"),
            ]),
            FieldRowPanel([
                FieldPanel('phone', classname="full"),
                FieldPanel('email', classname="full"),
            ]),
            FieldPanel('address', classname="full"),
            FieldPanel('hero_picture'),
            MultiFieldPanel([
                FieldPanel('github_link'),
                FieldPanel('facebook_link'),
                FieldPanel('linkedin_link'),
                FieldPanel('youtube_link'),
            ], heading="Redes Sociales"),
        ], heading="Hero"),
        MultiFieldPanel([
            FieldPanel('presentation_title'),
            FieldPanel('presentation_desc'),
            FieldPanel("cv_file")
        ], heading="Presentación"),
        MultiFieldPanel([
            FieldPanel('resume_title', classname="title"),
            FieldPanel('resume_body', classname="full"),
            FieldPanel("education"),
            FieldPanel("job_history"),
            FieldPanel("skills")
        ], heading="Curriculum", classname="collapsible collapsed"),
        MultiFieldPanel([
            FieldPanel('project_title', classname="title"),
            FieldPanel("projects")
        ], heading="Proyectos", classname="collapsible collapsed"),
        MultiFieldPanel([
            FieldPanel("testimonials")
        ], heading="Testimonios", classname="collapsible collapsed"),
        MultiFieldPanel([
            FieldPanel('courses_title', classname="title"),
            FieldPanel('courses_message', classname="full"),
            FieldPanel("courses")
        ], heading="Mis Cursos", classname="collapsible collapsed"),
        MultiFieldPanel([
            InlinePanel('form_fields', label="Form fields"),
            MultiFieldPanel([
                FieldRowPanel([
                    FieldPanel('from_address', classname="col6"),
                    FieldPanel('to_address', classname="col6"),
                ]),
                FieldPanel('subject'),
            ], "Email"),
        ], heading="Contactanos", classname="collapsible collapsed"),
        MultiFieldPanel([
            FieldPanel('footer_legend'),
            FieldPanel('tab_text'),
        ], heading='otra info', classname="collapsible collapsed")

    ]
