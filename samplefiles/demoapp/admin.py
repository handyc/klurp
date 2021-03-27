from django.contrib import admin

# Register your models here.

admin.site.site_header = "Demo Site";
admin.site.site_title = "Demo Site";

from .models import Dictionary
from .models import DictionaryEntry

@admin.register(Dictionary)
class DictionaryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)

@admin.register(DictionaryEntry)
class DictionaryEntryAdmin(admin.ModelAdmin):
    list_display = ('term1','term2','dictionary',)
    list_filter = ('term1','term2','dictionary',)
    fields = ('term1','term2','dictionary',)

