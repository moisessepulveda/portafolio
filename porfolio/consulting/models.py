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

from .models.commons import BodyContentBlock