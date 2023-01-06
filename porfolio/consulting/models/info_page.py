from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from .commons import BodyContentBlock


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
