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


class ContentBlockAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'position')
    list_editable = ('position',)


class FacilitatorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ToolAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}    
    list_display = ('name', 'type')
    list_editable = ('type',)


class TrainingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'date', 'link')


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PageAdmin)
admin.site.register(ContentBlock, ContentBlockAdmin)
admin.site.register(Facilitator, FacilitatorAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(Training, TrainingAdmin)