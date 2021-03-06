# Generated by Django 3.2.4 on 2021-08-10 14:05

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210810_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='castpage',
            name='cast_list',
            field=wagtail.core.fields.StreamField([('profile', wagtail.core.blocks.StructBlock([('first_name', wagtail.core.blocks.CharBlock()), ('surname', wagtail.core.blocks.CharBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('job_title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock()), ('links', wagtail.core.blocks.StreamBlock([('social_link', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock()), ('url', wagtail.core.blocks.URLBlock())]))]))]))]),
        ),
    ]
