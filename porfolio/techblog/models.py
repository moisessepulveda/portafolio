from django.db import models

# Create your models here.
from wagtail.admin.panels import MultiFieldPanel, FieldPanel, PageChooserPanel
from wagtail.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.users.models import UserProfile


class TechBlogHome(Page):
    hero_title = models.CharField(max_length=50, verbose_name='Título principal', default='Título')

    carrousel = StreamField([
        ('page', blocks.PageChooserBlock(page_type='techblog.BlogPage')),
    ], use_json_field=True, verbose_name='Carrusel', null=True, blank=False, min_num=1, max_num=3)

    blog_index_1 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    blog_index_1_page_count = models.IntegerField(default=1, verbose_name='¿Cuantas páginas de esta sección se mostrarán?')

    blog_index_2 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    blog_index_2_page_count = models.IntegerField(default=1,
                                                  verbose_name='¿Cuantas páginas de esta sección se mostrarán?')

    blog_index_3 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    blog_index_3_page_count = models.IntegerField(default=1,
                                                  verbose_name='¿Cuantas páginas de esta sección se mostrarán?')

    blog_index_4 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    blog_index_4_page_count = models.IntegerField(default=1,
                                                  verbose_name='¿Cuantas páginas de esta sección se mostrarán?')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_title'),
            FieldPanel('carrousel'),
            MultiFieldPanel([
                PageChooserPanel('blog_index_1', 'techblog.BlogIndex'),
                FieldPanel('blog_index_1_page_count'),
            ], heading='Publicaciones 1'),
            MultiFieldPanel([
                PageChooserPanel('blog_index_2', 'techblog.BlogIndex'),
                FieldPanel('blog_index_2_page_count'),
            ], heading='Publicaciones 2'),
            MultiFieldPanel([
                PageChooserPanel('blog_index_3', 'techblog.BlogIndex'),
                FieldPanel('blog_index_3_page_count'),
            ], heading='Publicaciones 3'),
            MultiFieldPanel([
                PageChooserPanel('blog_index_4', 'techblog.BlogIndex'),
                FieldPanel('blog_index_4_page_count'),
            ], heading='Publicaciones 4')
        ], heading='Sección principal'),
    ]


class BlogIndex(Page):
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)

    def get_context(self, request):
        # Filter by tag
        blog_pages = self.get_children().live().specific()

        # Update template context
        context = super().get_context(request)
        context['blog_pages'] = blog_pages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('description'),
    ]

    subpage_types = ['techblog.BlogPage']


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class BlogPage(Page):
    date = models.DateField("Fecha publicación")
    extract = RichTextField(verbose_name='Extracto', max_length=240, null=True, blank=False)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Portada',
    )

    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('quote', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('youtube_video', blocks.URLBlock()),
        ('gallery', blocks.ListBlock(ImageChooserBlock(), icon='image', label='Gallery')),
    ], use_json_field=True, verbose_name='Cuerpo de la publicación')

    content_panels = Page.content_panels + [
        FieldPanel('main_image'),
        FieldPanel('extract'),
        FieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
        ], heading="Información extra"),
    ]

    parent_page_type = ['techblog.BlogIndex']
    subpage_types = []
