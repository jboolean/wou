from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from .models import (
	ContentBlock,
	Facilitator,
	Tool,
	Training
)


class PageForm(FlatpageForm):
	class Meta:
		model = FlatPage
		exclude = []
		widgets = {
			'content' : TinyMCE(attrs={'cols': 100, 'rows': 15}),
		}

class PageAdmin(FlatPageAdmin):
	form = PageForm		


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PageAdmin)
admin.site.register(ContentBlock)
admin.site.register(Facilitator)
admin.site.register(Tool)
admin.site.register(Training)