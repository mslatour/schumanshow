from django.db import models
from wagtail.admin import blocks

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.models import Image
from wagtail.embeds.blocks import EmbedBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    splash_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    tagline = models.TextField(default='')
    sub_tagline = models.TextField(default='')

    body = RichTextField(default='')

    content_panels = Page.content_panels + [
        ImageChooserPanel('splash_image'),
        FieldPanel('tagline'),
        FieldPanel('sub_tagline'),
        FieldPanel('body'),
    ]

class CastMemberBlock(blocks.StructBlock):
    first_name = blocks.CharBlock()
    surname = blocks.CharBlock()
    photo = ImageChooserBlock(required=False)
    description = blocks.RichTextBlock()
    twitter = blocks.CharBlock()
    linkedin = blocks.CharBlock()

    class Meta:
        icon = 'user'

class CastPage(Page):
    intro = RichTextField(default='')

    cast_list = StreamField([('profile', CastMemberBlock())])

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel('cast_list'),
    ]

class MediaPage(Page):
    intro = RichTextField(default='')

    media_items = StreamField([('video', EmbedBlock()), ('image', ImageChooserBlock())])

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel('media_items'),
    ]

class BlogPage(Page):
    body = RichTextField(default='')

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

class BlogIndexPage(Page):
    intro = RichTextField(default='')

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    @property
    def blogs(self):
        # Get list of live blog pages that are descendants of this page
        blogs = BlogPage.objects.live().descendant_of(self)

        # Order by most recent date first
        blogs = blogs.order_by('first_published_at').reverse()

        return blogs
