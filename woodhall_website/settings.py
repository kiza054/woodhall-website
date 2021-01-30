"""
Django settings for woodhall_website project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os, django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY') or '0890a21f94a04c73d94a8654029271b72342c06a23056936'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')

ALLOWED_HOSTS = ['*', '127.0.0.1', '.ngrok.io', '.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'beavers.apps.BeaversConfig',
    'cubs.apps.CubsConfig',
    'scouts.apps.ScoutsConfig',
    'accounts.apps.AccountsConfig',
    'executive.apps.ExecutiveConfig',
    'main_website.apps.MainWebsiteConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_summernote',
    'taggit_helpers',
    'taggit_labels',
    'debug_toolbar',
    'crispy_forms',
    'storages',
    'taggit',
]

SITE_ID = 1
AUTH_USER_MODEL = 'accounts.User'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'woodhall_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'woodhall_website.wsgi.application'

# Media files (Images, PDF, docx, etc)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'


# Django Summernote Variables

X_FRAME_OPTIONS = 'SAMEORIGIN'
SUMMERNOTE_THEME = 'bs4'
SUMMERNOTE_CONFIG = {
    'iframe': True,
    'summernote': {
        # As an example, using Summernote Air-mode
        'airMode': False,
        # Change editor size
        #'width': '100%',
        'height': '400',
    },
    'codemirror': {
        'mode': 'htmlmixed',
        'lineNumbers': 'true',
    },
    'lazy': False,
    # You can add custom css for SummernoteWidget.
    'css': (
        '/static/css/summernote.css',
    ),
}

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Custom Login Function Variables

LOGIN_REDIRECT_URL = 'main_website_home'
LOGIN_URL = 'login'

# Custom Email Backend Variables

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')

# Amazon S3 Settings/Variables

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') #or 'AKIAXXDZN6ETRZCRER4T'
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY') #or '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'
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME') #or 'woodhall-website'

AWS_S3_FILE_OVERWRITE = False
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_DEFAULT_ACL = 'public-read'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# django_heroku Settings/Variables

django_heroku.settings(locals())