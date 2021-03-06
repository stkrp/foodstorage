from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.RatingList.as_view(), name='rating-list'),
    url(r'^(?P<pk>\d+)/$', views.RatingDetail.as_view(), name='rating-detail'),
]
