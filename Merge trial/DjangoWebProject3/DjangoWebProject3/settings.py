#"""
#Django settings for DjangoWebProject3 project.
#"""

#import os
#from crispy_forms.tests.test_settings import TEMPLATE_DEBUG
#PROJECT_ROOT = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

#DEBUG = True
#TEMPLATE_DEBUG = DEBUG
##TEMPLATE_DEBUG=True

## Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


## Quick-start development settings - unsuitable for production
## See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

## SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '49=262_iah#ofdh%aft(a=#*um*2ckei@t45yw)knb*rc_hm7z'

#ALLOWED_HOSTS = (
#    'localhost',
#)

#ADMINS = (
#    # ('Your Name', 'your_email@example.com'),
#)

#MANAGERS = ADMINS

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
#        'USER': '',
#        'PASSWORD': '',
#        'HOST': '',
#        'PORT': '',
#    }
#}

#LOGIN_URL = '/login'

## Local time zone for this installation. Choices can be found here:
## http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
## although not all choices may be available on all operating systems.
## On Unix systems, a value of None will cause Django to use the same
## timezone as the operating system.
## If running in a Windows environment this must be set to the same as your
## system time zone.
#TIME_ZONE = 'America/Chicago'

## Language code for this installation. All choices can be found here:
## http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'en-us'

#SITE_ID = 1

## If you set this to False, Django will make some optimizations so as not
## to load the internationalization machinery.
#USE_I18N = True

## If you set this to False, Django will not format dates, numbers and
## calendars according to the current locale.
#USE_L10N = True

## If you set this to False, Django will not use timezone-aware datetimes.
#USE_TZ = True

## Absolute filesystem path to the directory that will hold user-uploaded files.
## Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media').replace('\\', '/')

## URL that handles the media served from MEDIA_ROOT. Make sure to use a
## trailing slash.
## Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
#MEDIA_URL = '/media/'

## Absolute path to the directory static files should be collected to.
## Don't put anything in this directory yourself; store your static files
## in apps' "static/" subdirectories and in STATICFILES_DIRS.
## Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')

## URL prefix for static files.
## Example: "http://media.lawrence.com/static/"
#STATIC_URL = '/static/'

## Additional locations of static files
#TEMPLATE_DIRS = (
#    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
#    # Always use forward slashes, even on Windows.
#    # Don't forget to use absolute paths, not relative paths.
#    os.path.join(PROJECT_ROOT, 'templates').replace('\\', '/'),
#)



## List of finder classes that know how to find static files in
## various locations.
#STATICFILES_FINDERS = (
#    'django.contrib.staticfiles.finders.FileSystemFinder',
#    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
##    'django.contrib.staticfiles.finders.DefaultStorageFinder',
#)

## Make this unique, and don't share it with anybody.
#SECRET_KEY = 'n(bd1f1c%e8=_xad02x5qtfn%wgwpi492e$8_erx+d)!tpeoim'

## List of callables that know how to import templates from various sources.
#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.Loader',
#    'django.template.loaders.app_directories.Loader',
##     'django.template.loaders.eggs.Loader',
#)

##MIDDLEWARE_CLASSES = (
##    'django.middleware.common.CommonMiddleware',
##    'django.contrib.sessions.middleware.SessionMiddleware',
##    'django.middleware.csrf.CsrfViewMiddleware',
##    'django.contrib.auth.middleware.AuthenticationMiddleware',
##    'django.contrib.messages.middleware.MessageMiddleware',
##    # Uncomment the next line for simple clickjacking protection:
##    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
##)

#MIDDLEWARE_CLASSES = [
#    'django.middleware.security.SecurityMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
#    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#]

#ROOT_URLCONF = 'DjangoWebProject3.urls'

## Python dotted path to the WSGI application used by Django's runserver.
#WSGI_APPLICATION = 'DjangoWebProject3.wsgi.application'

##TEMPLATE_DIRS = (
##    # Put strings here, like "/home/html/django_templates" or
##    # "C:/www/django/templates".
##    # Always use forward slashes, even on Windows.
##    # Don't forget to use absolute paths, not relative paths.
##)

##INSTALLED_APPS = (
##    'django.contrib.auth',
##    'django.contrib.contenttypes',
##    'django.contrib.sessions',
##    'django.contrib.sites',
##    'django.contrib.messages',
##    'django.contrib.staticfiles',
##    'app',
##    # Uncomment the next line to enable the admin:
##    # 'django.contrib.admin',
##    # Uncomment the next line to enable admin documentation:
##    # 'django.contrib.admindocs',
##)

#INSTALLED_APPS = [
#    'django.contrib.admin',
#    'django.contrib.auth',
#    'django.contrib.sites',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.messages',
#    'django.contrib.staticfiles',
#    'crispy_forms',
#    'DjangoWebProject3',
#    'registration',
#]

## A sample logging configuration. The only tangible logging
## performed by this configuration is to send an email to
## the site admins on every HTTP 500 error when DEBUG=False.
## See http://docs.djangoproject.com/en/dev/topics/logging for
## more details on how to customize your logging configuration.
#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'filters': {
#        'require_debug_false': {
#            '()': 'django.utils.log.RequireDebugFalse'
#        }
#    },
#    'handlers': {
#        'mail_admins': {
#            'level': 'ERROR',
#            'filters': ['require_debug_false'],
#            'class': 'django.utils.log.AdminEmailHandler'
#        }
#    },
#    'loggers': {
#        'django.request': {
#            'handlers': ['mail_admins'],
#            'level': 'ERROR',
#            'propagate': True,
#        },
#    }
#}

## Specify the default test runner.
#TEST_RUNNER = 'django.test.runner.DiscoverRunner'



##TEMPLATES = [
##    {
##        'BACKEND': 'django.template.backends.django.DjangoTemplates',
##        'DIRS': [],
##        'APP_DIRS': True,
##        'OPTIONS': {
##            'context_processors': [
##                'django.template.context_processors.debug',
##                'django.template.context_processors.request',
##                'django.contrib.auth.context_processors.auth',
##                'django.contrib.messages.context_processors.messages',
##            ],
##        },
##    },
##]

#TTEMPLATES = [
#    {
#        'BACKEND': 'django.template.backends.django.DjangoTemplates',
#        'DIRS': [],
#        'APP_DIRS': True,
#        'OPTIONS': {
#            'context_processors': [
#                'django.template.context_processors.debug',
#                'django.template.context_processors.request',
#                'django.contrib.auth.context_processors.auth',
#                'django.contrib.messages.context_processors.messages',
#            ],
#        },
#    },
#]


#AUTH_PASSWORD_VALIDATORS = [
#    {
#        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#    },
#]

#CRISPY_TEMPLATE_PACK ='bootstrap3'


#    #django act redux settings
#ACCOUNT_ACTIVATION_DAYS = 7
#REGISTRATION_AUTO_LOGIN = True
#SITE_ID=1

#LOGIN_REDIRECT_URL='/' #at homepage if you wantit to profile the type : '/profile'
#########################################################################################
#"""
#Django settings for DjangoWebProject3 project.
#"""

#from os import path
#PROJECT_ROOT = path.dirname(path.abspath(path.dirname(__file__)))

#DEBUG = True
#TEMPLATE_DEBUG = DEBUG

#ALLOWED_HOSTS = (
#    'localhost',
#)

#ADMINS = (
#    # ('Your Name', 'your_email@example.com'),
#)

#MANAGERS = ADMINS

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': path.join(PROJECT_ROOT, 'db.sqlite3'),
#        'USER': '',
#        'PASSWORD': '',
#        'HOST': '',
#        'PORT': '',
#    }
#}

#LOGIN_URL = '/login'

## Local time zone for this installation. Choices can be found here:
## http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
## although not all choices may be available on all operating systems.
## On Unix systems, a value of None will cause Django to use the same
## timezone as the operating system.
## If running in a Windows environment this must be set to the same as your
## system time zone.
#TIME_ZONE = 'America/Chicago'

## Language code for this installation. All choices can be found here:
## http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'en-us'

#SITE_ID = 1

## If you set this to False, Django will make some optimizations so as not
## to load the internationalization machinery.
#USE_I18N = True

## If you set this to False, Django will not format dates, numbers and
## calendars according to the current locale.
#USE_L10N = True

## If you set this to False, Django will not use timezone-aware datetimes.
#USE_TZ = True

## Absolute filesystem path to the directory that will hold user-uploaded files.
## Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = path.join(PROJECT_ROOT, 'media').replace('\\', '/')

## URL that handles the media served from MEDIA_ROOT. Make sure to use a
## trailing slash.
## Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
#MEDIA_URL = '/media/'

## Absolute path to the directory static files should be collected to.
## Don't put anything in this directory yourself; store your static files
## in apps' "static/" subdirectories and in STATICFILES_DIRS.
## Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = path.join(PROJECT_ROOT, 'static').replace('\\', '/')

## URL prefix for static files.
## Example: "http://media.lawrence.com/static/"
#STATIC_URL = '/static/'

## Additional locations of static files
#TEMPLATE_DIRS = (
#    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
#    # Always use forward slashes, even on Windows.
#    # Don't forget to use absolute paths, not relative paths.
#    '<workspace>/tango_with_django_project/templates/',
#)



## List of finder classes that know how to find static files in
## various locations.
#STATICFILES_FINDERS = (
#    'django.contrib.staticfiles.finders.FileSystemFinder',
#    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
##    'django.contrib.staticfiles.finders.DefaultStorageFinder',
#)

## Make this unique, and don't share it with anybody.
#SECRET_KEY = 'n(bd1f1c%e8=_xad02x5qtfn%wgwpi492e$8_erx+d)!tpeoim'

## List of callables that know how to import templates from various sources.
#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.Loader',
#    'django.template.loaders.app_directories.Loader',
##     'django.template.loaders.eggs.Loader',
#)

#MIDDLEWARE_CLASSES = (
#    'django.middleware.common.CommonMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
#    # Uncomment the next line for simple clickjacking protection:
#    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
#)

#ROOT_URLCONF = 'DjangoWebProject3.urls'

## Python dotted path to the WSGI application used by Django's runserver.
#WSGI_APPLICATION = 'DjangoWebProject3.wsgi.application'

#TEMPLATE_DIRS = (
#    # Put strings here, like "/home/html/django_templates" or
#    # "C:/www/django/templates".
#    # Always use forward slashes, even on Windows.
#    # Don't forget to use absolute paths, not relative paths.
#)

#INSTALLED_APPS = (
#    #'django.contrib.auth',
#    #'django.contrib.contenttypes',
#    #'django.contrib.sessions',
#    #'django.contrib.sites',
#    #'django.contrib.messages',
#    #'django.contrib.staticfiles',
#    #'app',
#    ## Uncomment the next line to enable the admin:
#    ## 'django.contrib.admin',
#    ## Uncomment the next line to enable admin documentation:
#    ## 'django.contrib.admindocs',
#    'django.contrib.admin',
#    'django.contrib.auth',
#    'django.contrib.sites',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.messages',
#    'django.contrib.staticfiles',
#    'crispy_forms',
#    #'newsletter',
#    'registration',
#)

## A sample logging configuration. The only tangible logging
## performed by this configuration is to send an email to
## the site admins on every HTTP 500 error when DEBUG=False.
## See http://docs.djangoproject.com/en/dev/topics/logging for
## more details on how to customize your logging configuration.
#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'filters': {
#        'require_debug_false': {
#            '()': 'django.utils.log.RequireDebugFalse'
#        }
#    },
#    'handlers': {
#        'mail_admins': {
#            'level': 'ERROR',
#            'filters': ['require_debug_false'],
#            'class': 'django.utils.log.AdminEmailHandler'
#        }
#    },
#    'loggers': {
#        'django.request': {
#            'handlers': ['mail_admins'],
#            'level': 'ERROR',
#            'propagate': True,
#        },
#    }
#}

## Specify the default test runner.
#TEST_RUNNER = 'django.test.runner.DiscoverRunner'
##################################################
"""
Django settings for trydjango18 project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '49=262_iah#ofdh%aft(a=#*um*2ckei@t45yw)knb*rc_hm7z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

EMAIL_HOST = 'smtp.nabee@gmail.com'
EMAIL_HOST_USER = 'miina.nabeeh@gmail.com'
EMAIL_HOST_PASSWORD='1475963ina'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


''' 
If using gmail, you will need to
unlock Captcha to enable Django 
to  send for you:
https://accounts.google.com/displayunlockcaptcha
'''


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'DjangoWebProject3',
    'registration',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DjangoWebProject3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoWebProject3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR,"static_in_pro","static_root")



STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_in_pro","our_static"),
    #os.path.join(BASE_DIR, "static_in_env"),#not the right method to do so
    #os.path.join(BASE_DIR, "static_in_env"),
    #'/var/www/static/',
)
#dynamic by user
MEDIA_URL='/media/'

MEDIA_ROOT=os.path.join(BASE_DIR, "static_in_pro","media_root"),

#crispy form tag settings
CRISPY_TEMPLATE_PACK ='bootstrap3'


    #django act redux settings
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SITE_ID=1

LOGIN_REDIRECT_URL='/' #at homepage if you wantit to profile the type : '/profile'

TEMPLATE_DEBUG = DEBUG