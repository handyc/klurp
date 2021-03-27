from django.db import models

#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Home(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "999999999999999. Homes"

    name = models.CharField(max_length=2000, default="")

    def __str__(self):
        return self.name

class Bibliography(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Bibliographies"

    name = models.CharField(max_length=2000, default="")

    def __str__(self):
        return self.name

class BibliographyEntry(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Bibliography Entries"

    name = models.CharField(max_length=2000, default="")

    def __str__(self):
        return self.name

class Member(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Members"

    name = models.CharField(max_length=2000, default="", null=True, blank=True)
    email = models.CharField(max_length=500, default="", null=True, blank=True)
    bio = models.CharField(max_length=20000, default="", null=True, blank=True)
    pubs = models.CharField(max_length=20000, default="", null=True, blank=True)

    def __str__(self):
        return self.name

class NewsItem(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "News Items"

    name = models.CharField(max_length=2000, default="")

    def __str__(self):
        return self.name

class Resource(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Resources"

    name = models.CharField(max_length=2000, default="")

    def __str__(self):
        return self.name

class Language(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Languages"

    name = models.CharField(max_length=2000, default="")

    def __str__(self):
        return self.name

class Dictionary(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "01. Dictionaries"

    name = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name

class DictionaryEntry(models.Model):
    class Meta:
        ordering = ('term1','term2')
        verbose_name_plural = "02. Dictionary Entries"

    dictionary = models.ForeignKey('Dictionary', on_delete=models.SET_NULL, null=True, blank=True)

    term1 = models.CharField(max_length=200, default="")
    term2 = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.term1


