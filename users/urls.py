from django.conf.urls import url
from photos.views import UserPhotoList, UserRatingPhotoList
from ratings.views import UserRatingList, UserPhotoRatingList

from . import views


urlpatterns = [
    url(r'^$', views.UserList.as_view(), name='user-list'),
    url(r'^(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user-detail'),

    url(
        r'^(?P<user>\d+)/photos/$',
        UserPhotoList.as_view(),
        name='user-photo-list'
    ),
    url(
        r'^(?P<user>\d+)/photos/ratings/$',
        UserPhotoRatingList.as_view(),
        name='user-photo-rating-list'
    ),

    url(
        r'^(?P<user>\d+)/ratings/$',
        UserRatingList.as_view(),
        name='user-rating-list'
    ),
    url(
        r'^(?P<user>\d+)/ratings/photos/$',
        UserRatingPhotoList.as_view(),
        name='user-rating-photo-list',
    )
]
