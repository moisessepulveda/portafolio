from django.db import models

from wagtail.core import blocks
from wagtail.admin.panels import MultiFieldPanel, FieldPanel, FieldRowPanel
from wagtail.core.fields import StreamField
from wagtail.models import Page

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
