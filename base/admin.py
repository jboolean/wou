from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from .models import (
	ContentBlock,
	Facilitator,
    Practice,
    Reading,
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
    readonly_fields = ('url',)
    list_display = ('name', 'position', 'url')
    list_editable = ('position',)


class FacilitatorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('url',)
    list_display = ('name', 'url')


class ToolAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('url',)
    list_display = ('name', 'type', 'made_by', 'url')
    list_editable = ('type',)


class TrainingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('url',)
    list_display = ('name', 'date', 'link', 'url')


class ReadingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PracticeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PageAdmin)
admin.site.register(ContentBlock, ContentBlockAdmin)
admin.site.register(Facilitator, FacilitatorAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Reading, ReadingAdmin)
admin.site.register(Practice, PracticeAdmin)
