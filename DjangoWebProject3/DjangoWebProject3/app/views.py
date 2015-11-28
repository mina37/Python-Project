"""
Definition of views.
"""

from django.shortcuts import render,render_to_response
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.http.response import HttpResponse, HttpResponseRedirect
from app.models import *

def user(request):
    usrs=users.objects.all()
    return render_to_response('app/list of users.html',{'usrs':usrs})


def register(request):
    if request.method=='GET':
        form=usersforms();
        return render(request, 'app/WebPage1.html',{'form':form})
    elif request.method =='POST':
        form=usersforms(request.POST)
        form.save()
        return HttpResponseRedirect('')


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
