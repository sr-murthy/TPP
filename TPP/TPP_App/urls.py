from django.conf.urls import patterns, url

from TPP_App import views

urlpatterns = patterns( '',
    url( r'^$', views.welcome, name='welcome' ),
)
