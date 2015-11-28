"""
Definition of models.
"""

from django.db import models
from django.template.backends import django
from django import forms
from django.forms import ModelForm

# Create your models here.
class Artist(models.Model):
    name = models.CharField("artist",max_length = 50)
    year_formed = models.PositiveIntegerField()
class Album(models.Model):
    name = models.CharField("album",max_length = 50)
    artist = models.ForeignKey(Artist)
class users(models.Model):
    uname=models.CharField("Username",max_length=50)
    password=models.CharField("Password",max_length=50)
class usersforms(forms.ModelForm):
    class Meta:
        model = users
        fields = ['uname','password']
