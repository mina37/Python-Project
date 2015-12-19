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
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm

def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		# 	#print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email, message, full_name
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'youotheremail@email.com']
		contact_message = "%s: %s via %s"%( 
				form_full_name, 
				form_message, 
				form_email)
		some_html_message = """
		<h1>hello</h1>
		"""
		# send_mail(subject, 
		# 		contact_message, 
		# 		from_email, 
		# 		to_email, 
		# 		html_message=some_html_message,
		# 		fail_silently=True)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}
	return render(request, "forms.html", context)


#def user(request):
#    usrs=users.objects.all()
#    return render_to_response('app/list of users.html',{'usrs':usrs})

def watch(request):
    if request.method =='GET':
        form=commentform()
        c=comments.objects.all()
        return render(request, 'app/watch.html',{'form':form,'comm':c,'bold':"mickey"})
    elif request.method =='POST':
        form=commentform(request.POST)
        form.save()
        comm=comments.objects.last()
        comm.uname=request.user.username
        comm.save()
    return HttpResponseRedirect('/watch')
#def watch2(request):
#    c=comments.objects.all()
#    return render_to_response('app/watch.htm',{'comment':c})

#def watch(request):
#    #f = file()
#    #photo = f.objects.get(1)
    

#    return render_to_response('app/watch.html',{'bold':"2015-11-20_16_53_04-Settings"})
#    #return 0

def upload_file(request):
    # Handle file upload
    if request.method == 'POST':
        
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            
            newdoc = file(location = request.FILES['docfile'])#,name = request.FILES['docfile'].name)
            
            newdoc.save()
            return HttpResponseRedirect('/upload')
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('app.views.upload_file'))
            #return HttpResponseRedirect(reverse('app.views.upload_file'))
            return HttpResponseRedirect('/upload')
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


#def register(request):
#    res = ''
#    per=people.objects.all()
#    if request.method=='GET':
#        form=pforms();
#        return render(request, 'app/WebPage1.html',{'form':form})
#    elif request.method =='POST':
#        form=pforms(request.POST)
#        pers = people.objects.all()
#        #if form.Meta.model.email == people.email:
#        for p in pers:
#            for res in pforms(request.POST.get(4)):
#                res=res
#                if p.email == res:
#                    #res = "email already registered"
#                    #res = p.uname
#                    return render_to_response("app/WebPage1.html",{'res':"Hello"})
#                    return HttpResponseRedirect('')
#        form.save()
#        res = pforms(request.POST)
        
#        #return render_to_response("app/WebPage1.html",{'res':res})
#        return render_to_response("app/WebPage1.html",{'per':per})
#        return HttpResponseRedirect('/upload')


def home(request):
	title = 'Sign Up Now'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}


	if form.is_valid():
		#form.save()
		#print request.POST #not recommended
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		# if not instance.full_name:
		# 	instance.full_name = "Justin"
		instance.save()
		context = {
			"title": "Thank you"
		}

	return render(request, "home.html", context)

#def contact(request):
#    """Renders the contact page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/contact.html',
#        context_instance = RequestContext(request,
#        {
#            'title':'Contact',
#            'message':'Your contact page.',
#            'year':datetime.now().year,
#        })
#    )

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
