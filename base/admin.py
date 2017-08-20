from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from .models import (
	ContentBlock,
    Contributor,
	Facilitator,
    Practice,
    PracticeImage,
    PracticePdf,
    Reading,
	Tool,
	Training
)


class PracticeImageInline(admin.TabularInline):
    model = PracticeImage
    verbose_name = 'Practice Image'
    verbose_name_plural = 'Practice Images'
    fields = ('image', 'image_tag', 'order', 'is_primary')
    readonly_fields = ('image_tag',)
    extra = 1


class PracticePdfInline(admin.TabularInline):
    model = PracticePdf
    verbose_name = 'Practice PDF'
    verbose_name_plural = 'Practice PDFs'
    fields = ('pdf', 'name', 'order', 'is_primary')
    extra = 1


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
    list_display = ('name', 'position', 'url', 'is_on_main_site')
    list_editable = ('position', 'is_on_main_site')


class ContributorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


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
    fields = ('name', 'slug', 'contributors', 'description', 'trainings', 'readings', 'link', 'tags')
    inlines = [ PracticeImageInline, PracticePdfInline]


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PageAdmin)
admin.site.register(ContentBlock, ContentBlockAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Facilitator, FacilitatorAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Reading, ReadingAdmin)
admin.site.register(Practice, PracticeAdmin)
admin.site.register(PracticeImage)
admin.site.register(PracticePdf)

