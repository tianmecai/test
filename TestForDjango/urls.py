from django.conf.urls import patterns, include, url

from django.contrib import admin

from TestForDjango.views import hello

from TestForDjango import a

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TestForDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ('^hello/$',hello),
    ('^time/$',a.time),
    (r'^time/plus/(\d{1,2})$',a.time),
    url(r'^admin/', include(admin.site.urls)),
)
