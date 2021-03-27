from django.db import models

#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

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

