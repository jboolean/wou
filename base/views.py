from datetime import datetime, timedelta, time
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        if 'slug' in self.kwargs:
            context['slug'] = self.kwargs['slug']

        return context
