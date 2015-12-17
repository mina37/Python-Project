"""
Definition of views.
"""

from django.shortcuts import render,render_to_response
from django.http import HttpRequest
from django.template import RequestContext, context
from datetime import datetime
from django.http.response import HttpResponse, HttpResponseRedirect
from app.models import *
from django.core.files.uploadhandler import FileUploadHandler
from django.core.urlresolvers import reverse
from app.views import DocumentForm
from django.db import models
from django.template.base import Template


def user(request):
    usrs=users.objects.all()
    return render_to_response('app/list of users.html',{'usrs':usrs})

def watch(request):
    return render_to_response('app/watch.html',{'boldmessage':"2015-11-18 19_04_16-Alarms & Clock.png"})
    #return 0

def upload_file(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = file(location = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('app.views.upload_file'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = file.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'app/upload file dialogue.html',
        {'documents': file, 'form': form},
        context_instance=RequestContext(request)
    )


def register(request):
    res = ''
    per=people.objects.all()
    if request.method=='GET':
        form=pforms();
        return render(request, 'app/WebPage1.html',{'form':form})
    elif request.method =='POST':
        form=pforms(request.POST)
        pers = people.objects.all()
        #if form.Meta.model.email == people.email:
        for p in pers:
            for res in pforms(request.POST.get(4)):
                res=res
                if p.email == res:
                    #res = "email already registered"
                    #res = p.uname
                    return render_to_response("app/WebPage1.html",{'res':"Hello"})
                    return HttpResponseRedirect('')
        form.save()
        res = pforms(request.POST)
        
        #return render_to_response("app/WebPage1.html",{'res':res})
        return render_to_response("app/WebPage1.html",{'per':per})
        return HttpResponseRedirect('/upload')


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )
