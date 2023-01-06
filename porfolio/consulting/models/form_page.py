from django.db import models
from django.forms import widgets
from django.template.response import TemplateResponse
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.admin.panels import MultiFieldPanel, FieldPanel, FieldRowPanel, InlinePanel
from wagtail.core.fields import StreamField

from .commons import BodyContentBlock


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
