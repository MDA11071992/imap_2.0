from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateSchemeView, DetailSchemeView, CreateMapView, DetailMapView, CreateBuildingView, DetailBuildingView, CreateFloorView, DetailFloorView, CreateRoomView, RoomDetailView, FindPathView

urlpatterns = {
    url(r'^schemelist/$', CreateSchemeView.as_view(), name="create_scheme"),
    url(r'^schemelist/(?P<pk>[0-9]+)/?$', DetailSchemeView.as_view(), name="detail_scheme"),
    url(r'^map/$', CreateMapView.as_view(), name="create_map"),
    url(r'^map/(?P<pk>[0-9]+)/?$', DetailMapView.as_view(), name="detail_map"),
    url(r'^buildinglist/$', CreateBuildingView.as_view(), name="create_building"),
    url(r'^buildinglist/(?P<pk>[0-9]+)/?$', DetailBuildingView.as_view(), name="detail_building"),
    url(r'^floorlist/$', CreateFloorView.as_view(), name="create_floor"),
    url(r'^floorlist/(?P<pk>[0-9]+)/?$', DetailFloorView.as_view(), name="detail_floor"),
    url(r'^roomlist/$', CreateRoomView.as_view(), name="create_room"),
    url(r'^roomlist/(?P<pk>[0-9]+)/?$', RoomDetailView.as_view(), name="detail_room"),
    url(r'^findpath/$', FindPathView.as_view(), name="find_path"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)