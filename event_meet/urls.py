from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [url(r'^connect/', include('circly.urls', namespace="connect")),
               url(r'^admin/', include(admin.site.urls)),
]
