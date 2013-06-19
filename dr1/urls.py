# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site


import settings
import views


from django_authopenid.urls import urlpatterns as authopenid_urlpatterns
from registration.forms import RegistrationFormUniqueEmail

from djangobb_forum import settings as forum_settings

for i, rurl in enumerate(authopenid_urlpatterns):
    if rurl.name == 'registration_register':
        authopenid_urlpatterns[i].default_args.update({'form_class': RegistrationFormUniqueEmail})
        break

admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/favicon.ico'}),
    
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^settings/', include('livesettings.urls')),
    
    (r'^forum/account/', include('django_authopenid.urls')),
    (r'^forum/', include('djangobb_forum.urls', namespace='djangobb')),

    url(r'^$' , views.home_page),
    url(r'^news/$' , views.news_page),
    url(r'^news/(?P<page_name>[\w-]+)/$' , views.news_article_page),
    url(r'^docs/$' , views.docs_page),
    url(r'^docs/(?P<id>[\w-]+)/$' , views.docs_page),
    url(r'^company/(?P<page_name>[\w-]+)/$' , views.company_page),
    url(r'^(?P<page_name>[\w-]+)/$' , views.other_page),

)

if (forum_settings.PM_SUPPORT):
    urlpatterns += patterns('',
        (r'^forum/pm/', include('django_messages.urls')),
   )
    
if (settings.DEBUG):
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )