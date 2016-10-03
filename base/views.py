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
        context['content_blocks'] = ContentBlock.objects.all()
        context['tools'] = Tool.objects.all()
        context['trainings'] = Training.objects.all()
        context['facilitators'] = Facilitator.objects.all()
        if 'slug' in self.kwargs:
            context['slug'] = self.kwargs['slug']
        return context
