from __future__ import unicode_literals
from django.conf import settings
from django.db.models import *
from tinymce.models import HTMLField


class Base(Model):
    class Meta:
        abstract = True

    name = CharField(max_length=200)
    slug = CharField(max_length=200)
    created = DateTimeField(auto_now_add=True, editable=False)
    updated = DateTimeField(auto_now=True, editable=False)

    @property
    def url(self):
        return "%s/%s" % (settings.SITE_URL, self.slug)

    def __str__(self):
        return self.name


class ContentBlock(Base):
    class Meta:
        ordering = ['position', 'name']

    content = HTMLField()
    position = PositiveSmallIntegerField(null=True)


class Tool(Base):
    class Meta:
        ordering = ['type', 'name']

    TOOL_CHOICES = (
        ('use', 'In Use'),
        ('view', 'On View'),
        ('future', 'Future Tool'),
    )
    made_by = CharField(max_length=200, null=True)
    info = CharField(max_length=255, null=True)
    image = ImageField(null=True, upload_to='tools')
    type = CharField(
        max_length=8,
        choices=TOOL_CHOICES,
        default='use',
    )


class Facilitator(Base):
    class Meta:
        ordering = ['name']

    tools = ManyToManyField(Tool, blank=True)
    description = HTMLField()


class Training(Base):
    class Meta:
        ordering = ['date', 'name']

    date = DateTimeField()
    facilitators = ManyToManyField(Facilitator, blank=True)
    tools = ManyToManyField(Tool, blank=True)
    description = HTMLField(null=True, blank=True)
    link = URLField()
