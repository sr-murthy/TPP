from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^TPP_App/', include('TPP_App.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

