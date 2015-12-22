"""
Definition of models.
"""

from django.db import models
from django.template.backends import django
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime

# Create your models here.
#class Artist(models.Model):
#    name = models.CharField("artist",max_length = 50)
#    year_formed = models.PositiveIntegerField()
#class Album(models.Model):
#    name = models.CharField("album",max_length = 50)
#    artist = models.ForeignKey(Artist)
#class users(models.Model):
#    uname=models.CharField("Username",max_length=50)
#    password=models.CharField("Password",max_length=50)
#class usersforms(forms.ModelForm):
#    class Meta:
#        model = users
#        fields = ['uname','password']
class file(models.Model):
    name=models.CharField("file name",max_length=1000)
    location = models.FileField(upload_to="")#/Users/Mina37/documents/visual studio 2015/Projects/DjangoWebProject3/DjangoWebProject3/document")
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
#class people(models.Model):
#    fname=models.CharField("First Name",max_length = 50)
#    lname=models.CharField("Last Name",max_length = 50)
#    uname=models.CharField("User Name",max_length = 50)
#    passwords = models.CharField("Password",max_length = 50)
#    email=models.EmailField("Email")
#class pforms(forms.ModelForm):
#     class Meta:
#        model = people
#        fields = ['fname','lname','uname','passwords','email']
#class votes(models.Model):
#    uname=models.ForeignKey("user")
#    comment=models.ForeignKey(comments)
class comments(models.Model):
    comment=models.CharField(max_length=255)
    #vote=models.BooleanField()
    #vote=models.ForeignKey(votes)
    uname=models.CharField(max_length=255)
    #id=models.IntegerField(primary_key=True)
    #date=models.DateTimeField(null=True)
    #def __init__(self):
    #    self.date= datetime.now

class commentform(forms.ModelForm):
    class Meta:
        model = comments
        fields = ['comment']
#class voteform(forms.ModelForm):
#    class Meta:
#        model = comments
#        fields = ['vote']

class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #Python 3.3 is __str__
		return self.email
class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']