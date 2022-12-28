from django.db import models

# Create your models here.
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.models import Page


class HomeConsulting(Page):
    hero_title = models.CharField(max_length=50, verbose_name='Título principal', default='Título')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_title'),
        ], heading='Sección principal')
    ]
