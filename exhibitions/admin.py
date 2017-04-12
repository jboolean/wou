from django.contrib import admin
from .models import Exhibition

class ExhibitionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'start_date', 'end_date')


admin.site.register(Exhibition, ExhibitionAdmin)