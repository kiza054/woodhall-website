"""
Django settings for woodhall_website project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

import django_heroku

# from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# get_random_secret_key()
SECRET_KEY = os.environ.get('SECRET_KEY') or '0890a21f94a04c73d94a8654029271b72342c06a23056936'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('DEBUG_VALUE') or 'False')

ALLOWED_HOSTS = ['*', '127.0.0.1', '.ngrok.io', '.1stwoodhall.co.uk']

# Application definition

INSTALLED_APPS = [
    'beavers.apps.BeaversConfig',
    'cubs.apps.CubsConfig',
    'scouts.apps.ScoutsConfig',
    'accounts.apps.AccountsConfig',
    'executive.apps.ExecutiveConfig',
    'gallery.apps.GalleryConfig',
    'main_website.apps.MainWebsiteConfig',

    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',

    'django_summernote',
    'crispy_bootstrap5',
    'taggit_helpers',
    'taggit_labels',
    'debug_toolbar',
    'admin_reorder',
    'crispy_forms',
    'storages',
    'captcha',
    'taggit',
]

SITE_ID = 1 

AUTH_USER_MODEL = 'accounts.User'

CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

MIDDLEWARE = [
    'bugsnag.django.middleware.BugsnagMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
]

ROOT_URLCONF = 'woodhall_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = '/static/'

# Whitenoise Variables
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
WHITENOISE_MIMETYPES = {
    '.css': 'text/css',
    '.html': 'text/html'
}

# Django Admin-Reorder Settings

ADMIN_REORDER = (
    # Keep original label and models
    'beavers',
    'cubs',
    'scouts',
    'accounts',
    'executive',
    'main_website',
    'sites',
    'django_summernote',
)

# Django Summernote Variables

X_FRAME_OPTIONS = 'SAMEORIGIN'
SUMMERNOTE_THEME = 'lite'
SUMMERNOTE_CONFIG = {
    'iframe': True,
    'summernote': {
        'airMode': False,
        # Change editor size
        #'width': '100%',
        'height': '400',
        # Toolbar customization
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear', 'strikethrough', 'superscript', 'subscript']],
            ['fontname', ['fontname']],
            ['fontsize', ['fontsize']],
            ['forecolor', ['forecolor']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],
        'lang': 'en-GB',
    },
    # You can add custom css for SummernoteWidget.
    'css': (
        '/static/main_website/css/summernote/themes/woodhall/woodhall.css',
    ),
    'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': 'true',
            # You have to include theme file in 'css' or 'css_for_inplace' before using it.
            'theme': 'woodhall',
    },
    'lazy': False,
}

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# Logging with BugSnag

BUGSNAG = {
    'api_key': os.environ.get('BUGSNAG_API_KEY')
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'root': {
        'level': 'ERROR',
        'handlers': ['bugsnag'],
    },

    'handlers': {
        'bugsnag': {
            'level': 'INFO',
            'class': 'bugsnag.handlers.BugsnagHandler',
        },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Custom Login Function Variables

LOGIN_REDIRECT_URL = 'main_website_home'
LOGIN_URL = 'login'

# Custom Email Backend Variables

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True
#EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
#EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# MailJet SMTP Settings

EMAIL_BACKEND = 'django_mailjet.backends.MailjetBackend'
EMAIL_HOST = 'in-v3.mailjet.com'
MAILJET_API_KEY = os.environ.get('MAILJET_API_KEY')
MAILJET_API_SECRET = os.environ.get('MAILJET_API_SECRET')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_TIMEOUT = 30
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

# Google Maps API Settings

GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')

# Amazon S3 Settings/Variables
# When in development comment out lines 282-289
# When in production uncomment lines 282-289

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# django_heroku Settings/Variables

django_heroku.settings(locals()) 

# Django Celery Settings

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_TIMEZONE = TIME_ZONE

# Google reCAPTCHA Settings

RECAPTCHA_PUBLIC_KEY = str(os.environ.get('RECAPTCHA_PUBLIC_KEY'))
RECAPTCHA_PRIVATE_KEY = str(os.environ.get('RECAPTCHA_PRIVATE_KEY'))
RECAPTCHA_REQUIRED_SCORE = 0.9
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']