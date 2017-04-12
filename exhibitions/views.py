from datetime import datetime, timedelta, time
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Exhibition, ContentBlock


class IndexView(generic.TemplateView):
    template_name = 'exhibitions/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        exhibition = get_object_or_404(Exhibition, slug=self.kwargs['slug'])

        today = datetime.now().date()

        context['exhibition'] = exhibition
        context['trainings'] = exhibition.trainings.filter(date__gte=today)
        context['content_blocks'] = exhibition.content_blocks.all()
        context['tools'] = exhibition.tools.all()
        context['facilitators'] = exhibition.facilitators.all()
        context['site_url'] = settings.SITE_URL

        if 'slug' in self.kwargs:
            context['slug'] = self.kwargs['slug']

        return context


class PastView(generic.TemplateView):
    template_name = 'exhibitions/past.html'

    def get_context_data(self, **kwargs):
        context = super(PastView, self).get_context_data(**kwargs)

        exhibition = get_object_or_404(Exhibition, slug=self.kwargs['slug'])

        today = datetime.now().date()

        context['exhibition'] = exhibition
        context['trainings'] = exhibition.trainings.filter(date__lte=today).order_by('-date')
        context['content_blocks'] = exhibition.content_blocks.all()
        context['site_url'] = settings.SITE_URL

        return context
