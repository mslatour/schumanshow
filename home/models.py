from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.images.models import Image
from wagtail.admin.edit_handlers import FieldPanel
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
