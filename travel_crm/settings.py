"""
Django settings for travel_crm project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
# from apps.booking.serializers import BookingSerializer
# from rest_framework import serializers
import os
import datetime
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f)_sy=de0f7z*qs19&uodz1+vx@4i5**$xl=0hz&6qrrajqqqj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [ 'admin.bonholidays.com.np', 'crm.mountaintigernepal.com', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    # django admin dashboard
    'material',
    'material.admin',
    'material.admin.default',
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.utils',
    # 'storages',
    # custom apps
    'apps.accounts',
    'apps.blogs',
    'apps.enquiry',
    'apps.packages',
    'apps.payment',
    'apps.booking',
    'apps.logo',
    'apps.office',
    #third party apps
    'rest_framework',
    'rest_framework.authtoken',
    'imagekit',
    'ckeditor',
    'ckeditor_uploader',
    'corsheaders',
    'django_filters',
    'storages',
    'debug_toolbar',
    # 'easy_thumbnails',
    'image_cropping',
    # "taggit",
]

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

CKEDITOR_UPLOAD_PATH = "uploads/"

#ckeditor configs # todo
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'width': 1000,
        'height': 400
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # django cors headers
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    #addedforoperatorpackage
    # 'django.contrib.operator.middleware.CurrentSiteMiddleware',
]


CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    "http://localhost:8080",
    "http://localhost:3000",
    "http://27.34.13.130",
    "http://192.168.1.178:3000",
    "http://127.0.0.1:9000",
    "http://bonholidays.com.np",
    "https://bonholidays.com.np",
    "https://www.bonholidays.com.np",
)

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

ROOT_URLCONF = 'travel_crm.urls'

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

WSGI_APPLICATION = 'travel_crm.wsgi.application'

# Local/Development
DEBUG = True

# Database
if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
            # 'OPTIONS': {
            #     "init_command": "SET foreign_key_checks = 0;",
            # },
            'STORAGE_ENGINE': 'MyISAM / INNODB / ETC'
        }
    }
    AWS_ACCESS_KEY_ID = "AKIAYOTYKWMTSYHWDP74"
    AWS_SECRET_ACCESS_KEY = "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"
    AWS_FILE_EXPIRE = 200
    AWS_PRELOAD_METADATA = True
    AWS_QUERYSTRING_AUTH = True
    DEFAULT_FILE_STORAGE = 'travel_crm.utils.MediaRootS3BotoStorage'
    STATICFILES_STORAGE = 'travel_crm.utils.StaticRootS3BotoStorage'
    AWS_STORAGE_BUCKET_NAME = 'bonbucket'
    S3DIRECT_REGION = 'ap-southeast-1'
    S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
    MEDIA_ROOT = MEDIA_URL
    STATIC_URL = S3_URL + 'static/'
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
    two_months = datetime.timedelta(days=61)
    date_two_months_later = datetime.date.today() + two_months
    expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")
    AWS_HEADERS = {
        'Expires': expires,
        'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()),),
    }
    # Production
    DEBUG = False
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'traveldb',
            'USER': 'root',
            'PASSWORD': '1234',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'accounts.User'

# MATERIAL_ADMIN_SITE = {
#     'HEADER':  ('My site header'),  # Admin site header
#     'TITLE':  ('Bonholidays'),  # Admin site title
    # 'FAVICON':  'path/to/favicon',  # Admin site favicon (path to static should be specified)
    # 'MAIN_BG_COLOR':  'blue',  # Admin site main color, css color should be specified
    # 'MAIN_HOVER_COLOR':  'green',  # Admin site main hover color, css color should be specified
    # 'PROFILE_PICTURE':  'path/to/image',  # Admin site profile picture (path to static should be specified)
    # 'PROFILE_BG':  'path/to/image',  # Admin site profile background (path to static should be specified)
    # 'LOGIN_LOGO':  'path/to/image',  # Admin site logo on login page (path to static should be specified)
    # 'LOGOUT_BG':  'path/to/image',  # Admin site background on login/logout pages (path to static should be specified)
    # 'SHOW_THEMES':  True,  #  Show default admin themes button
    # 'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
    # 'NAVBAR_REVERSE': True,  # Hide side navbar by default
    # 'SHOW_COUNTS': True, # Show instances counts for each model
    # 'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
    #     'accounts': 'person',
    #     'blogs': 'assignment',
    #     'enquiry': 'video_call',
    #     'notifications': 'alarm',
    #     'packages': 'spa',
    #     'payment': 'attach_money',
    #     'reportings': 'bug_report',
    # },
    # 'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
    #     # 'travels': 'room', eg: does not work
    # }
# }
#
MATERIAL_ADMIN_SITE = {
    'HEADER':  "Bonholidays",  # Admin site header
    'TITLE':  "Bonholidays",  # Admin site title
#     # 'FAVICON':  'path/to/favicon',  # Admin site favicon (path to static should be specified)
#     # 'MAIN_BG_COLOR':  'color',  # Admin site main color, css color should be specified
#     'MAIN_HOVER_COLOR':  'color',  # Admin site main hover color, css color should be specified
#     'PROFILE_PICTURE':  'static/admin/img/icon-alert.svg',  # Admin site profile picture (path to static should be specified)
#     'PROFILE_BG':  'static/admin/img/gerrard.jpg',  # Admin site profile background (path to static should be specified)
#     # 'LOGIN_LOGO':  '',  # Admin site logo on login page (path to static should be specified)
#     # 'LOGOUT_BG':  'path/to/image',  # Admin site background on login/logout pages (path to static should be specified)
#     # 'SHOW_THEMES':  True,  #  Show default admin themes button
#     # 'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
#     # 'NAVBAR_REVERSE': True,  # Hide side navbar by default
    'SHOW_COUNTS': True, # Show instances counts for each model
#     # 'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
#     #     'sites': 'send',
    }
#     # 'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
#     #     'site': 'contact_mail',
#     # }
#


# REST Framework settings
REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
# 'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated', ),
    # for pagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    # for filter
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend',
                                # 'rest_framework_json_api.filters.QueryParameterValidationFilter',
                                # 'rest_framework_json_api.filters.OrderingFilter',
                                # 'rest_framework_json_api.django_filters.DjangoFilterBackend',
                                # 'rest_framework.filters.SearchFilter',
                                ]
}


# SMTP Mail service with decouple
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'bonaakash@gmail.com'
SERVER_EMAIL = 'bonaakash@gmail.com'
# EMAIL_HOST_PASSWORD = 'ovlpoqdkuiktqfki'
EMAIL_HOST_PASSWORD = 'qjpogyuvbjxxwzkn'
EMAIL_USE_TLS = True
EMAIL_USE_SLS = False
EMAIL_PORT = 587
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

#credentials
#bonaakash@gmail.com
#bon12345@
#9863266717
#saroj.aakashlabs@gmail.com
#2000-01-01





