from django.conf.urls import patterns, include, url
from django.conf import settings


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RegistroHoras.views.home', name='home'),
    # url(r'^RegistroHoras/', include('RegistroHoras.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'templates/js'}),


    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
