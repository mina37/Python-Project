﻿"""
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
class file(models.Model):
    name=models.CharField("file name",max_length=50)
    location = models.FileField(upload_to="documents/")
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
class people(models.Model):
    fname=models.CharField("First Name",max_length = 50)
    lname=models.CharField("Last Name",max_length = 50)
    uname=models.CharField("User Name",max_length = 50)
    passwords = models.CharField("Password",max_length = 50)
    email=models.EmailField("Email")
class pforms(forms.ModelForm):
     class Meta:
        model = people
        fields = ['fname','lname','uname','passwords','email']
class comments(models.Model):
    comment=models.CharField("Comment",max_length=255)
class commentform(forms.ModelForm):
    class Meta:
        model = comments
        fields = ['comment']
