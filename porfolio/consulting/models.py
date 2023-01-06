from django.db import models

# Create your models here.
from django.forms import widgets
from django.template.response import TemplateResponse
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.core import blocks
from wagtail.admin.panels import MultiFieldPanel, FieldPanel, FieldRowPanel, InlinePanel
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page


class BodyContentBlock(blocks.StreamBlock):
    h1 = blocks.CharBlock(form_classname="title")
    h2 = blocks.CharBlock(form_classname="title")
    h3 = blocks.CharBlock(form_classname="title")
    h4 = blocks.CharBlock(form_classname="title")
    paragraph = blocks.RichTextBlock(label="Parrafo")
    quote = blocks.RichTextBlock(label="Cita")
    image = ImageChooserBlock(label="Imagén")
    youtube_video = blocks.URLBlock(label="Video en youtube")
    gallery = blocks.ListBlock(ImageChooserBlock(), icon='image', label='Galería')

    class Meta:
        template = 'consulting/blocks/body_content_block.html'


class HomeConsulting(Page):
    # --- home sección 1 --------------------------------------------------------------------------------------------------------
    # elementos titulo página principal
    hero_title                 = models.CharField(max_length=50, verbose_name='Título principal', default='Título')
    hero_over_title            = models.CharField(max_length=50, verbose_name='texto sobre titulo principal', default='',blank=True)
    hero_title_description     = models.CharField(max_length=150, verbose_name='descripcion titulo principal', default='',blank=True)
    # boton redirección about
    hero_button_title          = models.CharField(max_length=50, verbose_name='texto boton titulo', default='',blank=True)
    hero_button_title_redirect = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    # imagen principal
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Imagen principal',
    )


    # --- home sección 2 --------------------------------------------------------------------------------------------------------
    hero_agile_develop              = models.CharField(max_length=50, verbose_name='item 1 titulo', default='item 1')
    hero_agile_develop_desc         = models.CharField(max_length=150, verbose_name='item descripción 1', default='')

    hero_information_security       = models.CharField(max_length=50, verbose_name='item 2 titulo', default='item 2')
    hero_information_security_desc  = models.CharField(max_length=150, verbose_name='item descripción 2', default='')

    hero_scalability                = models.CharField(max_length=50, verbose_name='item 3 titulo', default='item 3')
    hero_scalability_desc           = models.CharField(max_length=150, verbose_name='item descripción 3', default='')


    # --- home sección 3 --------------------------------------------------------------------------------------------------------
    hero_title_company         = models.CharField(max_length=100, verbose_name='nuestra compañia titulo', default='nuestra compañia titulo')
    hero_our_company           = models.CharField(max_length=100, verbose_name='nuestra compañia', default='nuestra compañia')
    hero_our_company_desc      = models.CharField(max_length=200, verbose_name='nuestra compañia descripción', default='nuestra compañia descripción')

    hero_company_success       = models.CharField(max_length=100, verbose_name='titulo success project', default='success project')
    hero_company_success_desc  = models.CharField(max_length=200, verbose_name='success project descripción', default='nuestra compañia descripción')

    hero_company_customer      = models.CharField(max_length=100, verbose_name='titulo customer review', default='customer review')
    hero_company_customer_desc = models.CharField(max_length=200, verbose_name='customer review descripción', default='nuestra compañia descripción')


    # --- home sección 4 --------------------------------------------------------------------------------------------------------
    hero_services_title        = models.CharField(max_length=100, verbose_name='servicios titulo', default='servicios titulo')
    hero_services_desc         = models.CharField(max_length=200, verbose_name='servicios descripcion', default='servicios descripcion')

     # boton redirección about
    hero_button_service           = models.CharField(max_length=50, verbose_name='texto boton service', default='',blank=True)
    hero_button_services_redirect = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )


    # --- home sección 5 --------------------------------------------------------------------------------------------------------
    hero_process_title   = models.CharField(max_length=100, verbose_name='titulo procesos', default='')
    hero_process_desc    = models.CharField(max_length=100, verbose_name='proceso descripción', default='')
    hero_process_step    = StreamField([
        ('card', blocks.StructBlock([
            ('title', blocks.TextBlock(label='titulo')),
            ('subtitle', blocks.TextBlock(label='subtitulo')),
            ('description', blocks.RichTextBlock(label='descripcion')),
            ])
        )
     ],  null=True, use_json_field=True)




    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_over_title'),
            FieldPanel('hero_title'),
            FieldPanel('hero_title_description'),
            FieldPanel('hero_image'),
            FieldRowPanel([
                FieldPanel('hero_button_title'),
                FieldPanel('hero_button_title_redirect')
            ])
        ], heading='Sección principal'),

        MultiFieldPanel([
            FieldPanel('hero_agile_develop'),
            FieldPanel('hero_agile_develop_desc'),
            FieldPanel('hero_information_security'),
            FieldPanel('hero_information_security_desc'),
            FieldPanel('hero_scalability'),
            FieldPanel('hero_scalability_desc'),

        ], heading='seccion 2'),

        MultiFieldPanel([
            FieldPanel('hero_title_company'),
            FieldPanel('hero_our_company'),
            FieldPanel('hero_our_company_desc'),
            FieldPanel('hero_company_success'),
            FieldPanel('hero_company_success_desc'),
            FieldPanel('hero_company_customer'),
            FieldPanel('hero_company_customer_desc'),

        ], heading='seccion 3'),

        MultiFieldPanel([
            FieldPanel('hero_services_title'),
            FieldPanel('hero_services_desc'),
            FieldRowPanel([
                FieldPanel('hero_button_service'),
                FieldPanel('hero_button_services_redirect')
            ])

        ], heading='seccion 4'),

        MultiFieldPanel([
            FieldPanel('hero_process_title'),
            FieldPanel('hero_process_desc'),
            FieldPanel('hero_process_step'),

        ], heading='seccion 5'),
    ]


class ServiceConsultingPage(Page):
    hero_title = models.CharField(max_length=50, null=True, blank=False,
                                  verbose_name='Título del servicio')

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Imagen principal',
    )

    body = StreamField(BodyContentBlock(),
                       use_json_field=True,
                       verbose_name='Descripción del servicio',
                       null=True, blank=False)

    side_block_title = models.CharField(max_length=30,
                                        verbose_name='Título bloque del costado',
                                        default='Otros servicios')

    contact_us_title = models.CharField(max_length=30,
                                        verbose_name='Título de contactanos',
                                        default='¿Tienes alguna duda?')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_title'),
            FieldPanel('hero_image'),
        ], heading='Sección principal'),
        FieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('side_block_title'),
            FieldPanel('contact_us_title'),
        ], heading='información del costado'),
    ]

    class Meta:
        verbose_name = 'Página de servicio'

    def get_context(self, request):
        # Filter by tag
        other_services = ServiceConsultingPage.objects.exclude(pk=self.pk).all()[:5]

        # Update template context
        context = super().get_context(request)
        context['other_services'] = other_services
        return context


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractEmailForm):

    def get_landing_page_template(self, *args, **kwargs):
        return 'consulting/success_form.html'

    def render_landing_page(self, request, form_submission=None, *args, **kwargs):
        """
        Renders the landing page.

        You can override this method to return a different HttpResponse as
        landing page. E.g. you could return a redirect to a separate page.
        """
        context = self.get_context(request)
        context["form_submission"] = form_submission
        context['stream_data'] = self.success_body
        return TemplateResponse(
            request, self.get_landing_page_template(request), context
        )

    body = StreamField(BodyContentBlock(), use_json_field=True, verbose_name='Descripción',
                       null=True, blank=False)

    form_button_text = models.CharField('Texto del botón', default='Enviar', max_length=50)

    success_body = StreamField(BodyContentBlock(), use_json_field=True,
                               verbose_name='Cuerpo de la página de éxito', null=True, blank=False)

    bottom_body = StreamField(BodyContentBlock(),
                              use_json_field=True,
                              verbose_name='Cuerpo debaje del formulario',
                              null=True, blank=True)

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        for name, field in form.fields.items():
            if any([isinstance(field.widget, widgets.TextInput),
                    isinstance(field.widget, widgets.NumberInput),
                    isinstance(field.widget, widgets.EmailInput),
                    isinstance(field.widget, widgets.Textarea)]):
                field.widget.attrs.update({'placeholder': field.label})

        return form

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('body'),
        InlinePanel('form_fields', label="Campos"),
        FieldPanel('form_button_text', classname='collapsible collapsed'),
        MultiFieldPanel([
            FieldPanel('success_body'),
        ], heading='información de éxito', classname='collapsible collapsed'),
        MultiFieldPanel([
            FieldPanel('bottom_body'),
        ], heading='información debajo del formulario', classname='collapsible collapsed'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    class Meta:
        verbose_name = 'Página con formulario'


class InfoPage(Page):
    body = StreamField(BodyContentBlock(),
                       use_json_field=True,
                       verbose_name='Cuerpo de la página',
                       null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = 'Página de información'
