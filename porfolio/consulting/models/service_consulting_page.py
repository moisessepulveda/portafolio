from django.db import models
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.core.fields import StreamField
from wagtail.models import Page
from .commons import BodyContentBlock


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
