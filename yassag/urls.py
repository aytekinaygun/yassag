from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yassag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('dashboard.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^reg/', include('devices_registration.urls')), # device_registration apps url's
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += staticfiles_urlpatterns()