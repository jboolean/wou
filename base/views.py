from datetime import datetime, timedelta, time
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from taggit.models import Tag
from .models import Practice, Reading

class IndexView(generic.TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['practices'] = Practice.objects.all()

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
        context['readings'] = readingsQuerySet
        context['practices'] = Practice.objects.filter(readings__in=readingsQuerySet)

        return context


class PracticeDetailView(generic.DetailView):
    template_name = 'base/practice-detail.html'
    model = Practice
