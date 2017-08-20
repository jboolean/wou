from __future__ import unicode_literals
from django.conf import settings
from django.db.models import *
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import format_html
from tinymce.models import HTMLField
from taggit.managers import TaggableManager


@python_2_unicode_compatible
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


class BaseImage(Model):
    class Meta:
        abstract = True

    image = ImageField(upload_to='images', verbose_name='Image')
    order = PositiveSmallIntegerField(default=0)
    is_primary = BooleanField(default=False)
    created = DateTimeField(auto_now_add=True, editable=False)
    updated = DateTimeField(auto_now=True, editable=False)

    @property
    def image_tag(self):
        return format_html('<img src="/static/uploads/%s" height="100" />' % self.image)


class ContentBlock(Base):
    class Meta:
        ordering = ['position', 'name']

    content = HTMLField()
    position = PositiveSmallIntegerField(null=True)
    is_on_main_site = BooleanField(default=True)


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
    pdf = FileField(upload_to='texts', blank=True, null=True)
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


class Reading(Base):
    class Meta:
        ordering = ['name']

    pdf = FileField(upload_to='texts', blank=True, null=True)
    tags = TaggableManager()


class Contributor(Base):
    class Meta:
        ordering = ['name']

    pass


class Practice(Base):
    class Meta:
        ordering = ['name']

    contributor = ForeignKey(Contributor)
    description = HTMLField(null=True, blank=True)
    tools = ManyToManyField(Tool, blank=True)
    trainings = ManyToManyField(Training, blank=True)
    readings = ManyToManyField(Reading, blank=True)
    link = URLField()
    tags = TaggableManager()

    @property
    def primary_image(self):
        qs = self.practiceimage_set.filter(is_primary=1)
        if len(qs) > 0:
            return qs[0]
        return None


class PracticeImage(BaseImage):
    practice = ForeignKey('Practice')
