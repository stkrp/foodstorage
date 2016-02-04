from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.PhotoList.as_view(), name='photo-list'),
    url(r'^(?P<pk>\d+)/$', views.PhotoDetail.as_view(), name='photo-detail'),
]
