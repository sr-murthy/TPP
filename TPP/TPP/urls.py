from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url( r'^TPP_App/', include( 'TPP_App.urls' ) ),
    url( r'^admin/', include( admin.site.urls ) ),
)
