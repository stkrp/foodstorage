from django.conf.urls import url
from ratings.views import PhotoRatingList
from users.views import PhotoRatingUserList

from . import views


urlpatterns = [
    url(r'^$', views.PhotoList.as_view(), name='photo-list'),
    url(r'^(?P<pk>\d+)/$', views.PhotoDetail.as_view(), name='photo-detail'),

    url(
        r'^(?P<photo>\d+)/ratings/$',
        PhotoRatingList.as_view(),
        name='photo-rating-list'
    ),

    url(
        r'^(?P<photo>\d+)/ratings/users/$',
        PhotoRatingUserList.as_view(),
        name='photo-rating-user-list'
    )
]
