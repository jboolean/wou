from datetime import datetime, timedelta, time
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import (
	ContentBlock,
	Facilitator,
	Tool,
	Training
)


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        today = datetime.now().date()

        context['trainings'] = Training.objects.filter(date__gte=today)
        context['content_blocks'] = ContentBlock.objects.all()
        context['tools'] = Tool.objects.all()
        context['facilitators'] = Facilitator.objects.all()
        context['site_url'] = settings.SITE_URL

        if 'slug' in self.kwargs:
            context['slug'] = self.kwargs['slug']

        return context


class PastView(generic.TemplateView):
    template_name = 'past.html'

    def get_context_data(self, **kwargs):
        context = super(PastView, self).get_context_data(**kwargs)

        today = datetime.now().date()

        context['trainings'] = Training.objects.filter(date__lte=today)
        context['content_blocks'] = ContentBlock.objects.all()
        context['site_url'] = settings.SITE_URL

        return context
