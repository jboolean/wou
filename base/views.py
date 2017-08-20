from datetime import datetime, timedelta, time
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from taggit.models import Tag
from .models import (
    Contributor,
    Practice,
    Reading,
    Training,
    ContentBlock
)

class IndexView(generic.TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        today = datetime.now().date()

        context['contributors'] = Contributor.objects.all()
        context['practices'] = Practice.objects.all()
        context['trainings'] = Training.objects.filter(date__gte=today)
        context['content_blocks'] = ContentBlock.objects.filter(is_on_main_site=True)

        if 'slug' in self.kwargs:
            context['slug'] = self.kwargs['slug']

        return context


class TagDetailView(generic.TemplateView):
    template_name = 'base/tag-detail.html'
    model = Tag

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)

        tag = get_object_or_404(Tag, slug=self.kwargs['slug'])

        readingsQuerySet = Reading.objects.filter(tags__slug__in=[tag.slug])
        practiceQuerySet = Practice.objects.filter(readings__in=readingsQuerySet)
        contributorQuerySet = Contributor.objects.filter(practice__in=practiceQuerySet)

        context['readings'] = readingsQuerySet
        context['practices'] = practiceQuerySet
        context['contributors'] = contributorQuerySet
        context['content_blocks'] = ContentBlock.objects.filter(is_on_main_site=True)
        context['tag'] = tag

        return context


class PracticeDetailView(generic.DetailView):
    template_name = 'base/practice-detail.html'
    model = Practice

    def get_context_data(self, **kwargs):
        context = super(PracticeDetailView, self).get_context_data(**kwargs)

        today = datetime.now().date()

        context['contributors'] = Contributor.objects.all()
        context['practices'] = Practice.objects.all()
        context['trainings'] = Training.objects.filter(date__gte=today)
        context['content_blocks'] = ContentBlock.objects.filter(is_on_main_site=True)

        if 'slug' in self.kwargs:
            context['slug'] = self.kwargs['slug']

        return context
