"""katyams URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import home.views
from django.utils.translation import ugettext_lazy as _

urlpatterns = [

    #url(r'^$', home.views.index),
    #url(r'^contact/$', home.views.contact),
    url(r'^contact/', include('contact_form.urls')),
    #url(r'^about/$', home.views.about),
    #url(r'^projects/$', home.views.projects),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns

