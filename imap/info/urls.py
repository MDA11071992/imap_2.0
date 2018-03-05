from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import ServiceView, ServiceDetailView, RoomView, RoomDetailView, TherapyView, TherapyDetailView, SubTherapyDetailView, AdvertisementView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^servicelist/$', ServiceView.as_view(), name="create_service"),
    url(r'^servicelist/(?P<pk>[0-9]+)/?$', ServiceDetailView.as_view(), name="service_detail"),
    url(r'^roomlist/$', RoomView.as_view(), name="create_room"),
    url(r'^roomlist/(?P<pk>[0-9]+)/?$', RoomDetailView.as_view(), name="room_detail"),
    url(r'^therapylist/$', TherapyView.as_view(), name="create_therapy"),
    url(r'^therapylist/(?P<pk>[0-9]+)/?$', TherapyDetailView.as_view(), name="therapy_detail"),
    url(r'^subtherapylist/(?P<pk>[0-9]+)/?$', SubTherapyDetailView.as_view(), name="subtherapy_detail"),
    url(r'^adver/$', AdvertisementView.as_view(), name="advertisement"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
