from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


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