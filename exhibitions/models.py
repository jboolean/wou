from __future__ import unicode_literals
from django.conf import settings
from django.db.models import *
from tinymce.models import HTMLField
from base.models import Base, ContentBlock, Tool, Facilitator, Training

class Exhibition(Base):
    class Meta:
        ordering = ['start_date', 'name']

    name = CharField(max_length=200, null=True)
    slug = SlugField(max_length=200)
    start_date = DateTimeField()
    end_date = DateTimeField()
    description = HTMLField(null=True)
    content_blocks = ManyToManyField(ContentBlock, blank=True, null=True)
    tools = ManyToManyField(Tool, blank=True)
    facilitators = ManyToManyField(Facilitator, blank=True)
    trainings = ManyToManyField(Training, blank=True)
    link = URLField(null=True, blank=True)
