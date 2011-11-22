
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

import csr.views, accounts.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', csr.views.index, name='index'),
    url(r'secure/$', csr.views.secure),
    url(r'^accounts/login/', accounts.views.login),
    url(r'^accounts/logout/', accounts.views.logout),
    # url(r'^accounts/', include(auth.urls)),
    # url(r'^CustomerReference/', include('CustomerReference.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
