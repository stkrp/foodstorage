from django.conf.urls import url
from photos.views import UserPhotoList

from . import views


urlpatterns = [
    url(r'^$', views.UserList.as_view(), name='user-list'),
    url(r'^(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user-detail'),

    url(
        r'^(?P<user>\d+)/photos/$',
        UserPhotoList.as_view(),
        name='user-photo-list'
    ),
]
