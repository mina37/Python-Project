"""
Definition of urls for DjangoWebProject3.
"""

from datetime import datetime
from django.conf.urls import patterns, url,include
#from app.forms import BootstrapAuthenticationForm
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
admin.autodiscover()


# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()
document_root=settings.MEDIA_ROOT
urlpatterns = patterns('',
                      # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                    url(r'^admin/', include(admin.site.urls)),
      #((r'^', include('DjangoWebProject3.urls')),) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
#    (r'^', include('DjangoWebProject3.urls'),
#) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),                  
    ## Examples:
    #url(r'watch','app.views.watch3',name='watch'),
    #url(r'watch','app.views.watch2',name='watch'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'watch','app.views.watch',name='watch'),
    url(r'upload','app.views.upload_file', name = 'upload'),
    #url(r'^users$','app.views.user', name = 'users'),
    #url(r'^register$','app.views.register',name='register'),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    #url(r'^login/$',
    #    'django.contrib.auth.views.login',
    #    {
    #        'template_name': 'app/login.html',
    #        'authentication_form': BootstrapAuthenticationForm,
    #        'extra_context':
    #        {
    #            'title':'Log in',
    #            'year':datetime.now().year,
    #        }
    #    },
    #    name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
     

    # Uncomment the next line to enable the admin:
    
)
#urlpatterns += staticfiles_urlpatterns()
#if settings.DEBUG:
urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True }),)