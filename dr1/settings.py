# -*- coding: utf-8 -*-
import os
from os.path import abspath, join, dirname

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
)

MANAGERS = ADMINS
PROJECT_ROOT = abspath(join(dirname(__file__), "../"))
LOGIN_URL = '/login'

DATE_FORMAT = '%d.%m.%Y'
DATETIME_FORMAT = '%d.%m.%Y'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dr1',   # Or path to database file if using sqlite3.
        'USER': 'dr1',                      # Not used with sqlite3.
        'PASSWORD': 'dr1',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'Ru-ru'

SITE_ID = 1


USE_I18N = True

USE_L10N = True

MEDIA_ROOT = MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'
ADMIN_TOOLS_THEMING_CSS = 'css/admin.css'


STATIC_ROOT = STATICFILES_ROOT = os.path.join(PROJECT_ROOT, 'static')


STATIC_URL = STATICFILES_URL = '/static/'
AUTH_PROFILE_MODULE = 'users.UserProfile'
ADMIN_TOOLS_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'

STATICFILES_DIRS = (
                    os.path.join(PROJECT_ROOT, 'site_static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '8bbd(7##fnhjww&_1-m4s_20f@h(av8$ast1c(rtdsp38)2b30'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django_authopenid.context_processors.authopenid',
    'messages.context_processors.inbox',
    'djangobb_forum.context_processors.forum_settings',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django_authopenid.middleware.OpenIDMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'djangobb_forum.middleware.LastLoginMiddleware',
    'djangobb_forum.middleware.UsersOnline',
)

ROOT_URLCONF = 'dr1.urls'

TEMPLATE_DIRS = (
                 os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',    
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'ckeditor',
    'filebrowser',
    'livesettings',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'sorl.thumbnail',
    'feincms',
    'mptt',
    'feincms.module.medialibrary',
    
    'registration',
    'pagination',
    'django_authopenid',
    'djangobb_forum',
    'haystack',
    'messages',
    
    'pages',
    'news',
    'slideshow',
    'docs',
    'company',
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.requdr1': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

FILE_UPLOAD_MAX_MEMORY_SIZE = 7864320
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar':
           [
                ['Source', '-', 'Templates'],
                ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
                ['Undo', 'Redo', ],
                ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'],
                ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
                ['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar'],
                ['RemoveFormat', 'Bold','Italic','Underline','Strike','-','Subscript','Superscript'],
                ['Styles','Format','FontSize', 'TextColor','BGColor'],
                ['Link','Unlink',],
                ['Maximize', 'ShowBlocks'],
            ],
        'width': 1056,
        'height': 200,
        'toolbarCanCollapse': True,
        'resize_enabled': True
    }
}


CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'uploads')
CKEDITOR_MEDIA_PREFIX = '/media/ckeditor/'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'noreply@webgenesis.ru'
EMAIL_HOST_PASSWORD = 'noreply13'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Haystack settings
HAYSTACK_CONNECTIONS = {
    'default': {
    'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(PROJECT_ROOT, 'djangobb_index'),
        'STORAGE': 'file',
        'POST_LIMIT': 128 * 1024 * 1024,
        'INCLUDE_SPELLING': True,
        'BATCH_SIZE': 100,
        'EXCLUDED_INDEXES': ['thirdpartyapp.search_indexes.BarIndex'],
    }
}
#HAYSTACK_SITECONF = 'search_sites'
#HAYSTACK_SEARCH_ENGINE = 'whoosh'
#HAYSTACK_WHOOSH_PATH = os.path.join(PROJECT_ROOT, 'djangobb_index')

# Account settings
ACCOUNT_ACTIVATION_DAYS = 10
LOGIN_REDIRECT_URL = '/forum/'
LOGIN_URL = '/forum/account/signin/'

#Cache settings
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

try:
    from dev import *
except:
    pass
