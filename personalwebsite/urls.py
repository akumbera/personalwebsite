from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


from blog.views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'personalwebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', homepage),
    url(r'^about/$', aboutpage),
    url(r'^resume/$', resumepage),
    url(r'^submit/$', addvideo),
    url(r'^submit/success/$', successpage),
    url(r'^video/(?P<title>\w+)/$', videopost),
)
