from django.db import models

# Create your models here.
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.models import Page


class HomeConsulting(Page):
    hero_title = models.CharField(max_length=50, verbose_name='Título principal', default='Título')

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Imagen principal',
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_title'),
            FieldPanel('hero_image'),
        ], heading='Sección principal'),
    ]


class ServiceConsultingPage(Page):
    description = models.TextField()

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('description')
        ])
    ]
