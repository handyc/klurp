from .models import DictionaryEntry
from .models import Dictionary
from .models import Language
from .models import Resource
from .models import NewsItem
from .models import Member
from .models import BibliographyEntry
from .models import Bibliography
from .models import Home
from django.contrib import admin

# Register your models here.

admin.site.site_header = "Demo Site"
admin.site.site_title = "Demo Site"


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)


@admin.register(Bibliography)
class BibliographyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)


@admin.register(BibliographyEntry)
class BibliographyEntryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'bio', 'pubs',)
    list_filter = ('name',)
    fields = ('name', 'email', 'bio', 'pubs',)


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)


@admin.register(Dictionary)
class DictionaryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)


@admin.register(DictionaryEntry)
class DictionaryEntryAdmin(admin.ModelAdmin):
    list_display = ('term1', 'term2', 'dictionary',)
    list_filter = ('term1', 'term2', 'dictionary',)
    fields = ('term1', 'term2', 'dictionary',)
