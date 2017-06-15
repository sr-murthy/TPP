from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^SmallGroupInfo/(?P<GAP_ID>([0-9]+,[0-9]+))/$', views.small_group_info, name='small_group_info')
]