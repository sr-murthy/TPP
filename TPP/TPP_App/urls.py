from django.conf.urls import patterns, url

from TPP_App import views

urlpatterns = patterns( '',
    url( r'^$', views.welcome, name='welcome' ),
    url( r'^(?P<GAP_ID>\d+)/$', views.small_group_info, name='small_group_info' ),
)
