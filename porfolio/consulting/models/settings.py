from django.db import models

# Create your models here.
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField

@register_setting
class GeneralInfo(BaseSetting):
    enterprise_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Logo de la empresa',
    )
    home_page = models.ForeignKey(
        'wagtailcore.Page', 
        null=True, 
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Página de inicio',
        blank=True,
        help_text='¿Cual será la página principal del sitio?'
    )
    enterprise_name = models.CharField(verbose_name='Nombre de la empresa', max_length=100)
    contact_phone = models.CharField(verbose_name='Teléfono de contacto', max_length=100)
    contact_email = models.EmailField(verbose_name='Correo de contacto', max_length=255)
    
    # social media

    facebook_link = models.URLField(verbose_name='Enlace a facebook', null=True, blank=True)
    instagram_link = models.URLField(verbose_name='Enlace a instagram', null=True, blank=True)
    twitter_link = models.URLField(verbose_name='Enlace a twitter', null=True, blank=True)
    linkedin_link = models.URLField(verbose_name='Enlace a linked in', null=True, blank=True)

    footer_resume = models.TextField(verbose_name='Reseña al pie de página', null=True, blank=True)
    

    contact_page = models.ForeignKey(
        'wagtailcore.Page', 
        null=True, 
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Página de contacto',
        blank=True,
    )


    terms_page = models.ForeignKey(
        'wagtailcore.Page', 
        null=True, 
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Página de términos y condiciones',
        blank=True,
    )

    privacy_page = models.ForeignKey(
        'wagtailcore.Page', 
        null=True, 
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Página de privacidad',
        blank=True,
    )

    footer_urls = StreamField([
        ('url', blocks.StructBlock([
            ('label', blocks.CharBlock(max_length=50, label="Etiqueta")),
            ('urls', blocks.PageChooserBlock(label="URL")),
        ], label="Enlace"))
    ], default='', null=True, blank=True, use_json_field=True, verbose_name='Enlaces al pie de página')


    class Meta:
        verbose_name = 'Configuración general página'