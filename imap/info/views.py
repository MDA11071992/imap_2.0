from django.http import HttpResponse

from .models import Service, Room, Therapy, SubTherapy, Advertisement
from .serializers import ServiceSerializer, ServiceNameSerializer, RoomSerializer, RoomNameSerializer, TherapySerializer, TherapyNameSerializer,  SubTherapySerializer, AdvertisementSerializer
from rest_framework import generics


def index(request):
    return HttpResponse('<a href="servicelist">servicelist/</a><br>'
                        '<a href="roomlist">roomlist/</a><br>'
                        '<a href="therapylist">therapylist/</a><br>'
                        '<a href="therapylist/sub">therapylist/sub/</a>')


class ServiceView(generics.ListCreateAPIView):
    queryset = Service.objects.order_by('name')
    serializer_class = ServiceNameSerializer

    def perform_create(self, serializer):
        serializer.save()

class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.order_by('name')
    serializer_class = ServiceSerializer


class RoomView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomNameSerializer

    def perform_create(self, serializer):
        serializer.save()

class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class TherapyView(generics.ListCreateAPIView):
    queryset = Therapy.objects.order_by('name')
    serializer_class = TherapyNameSerializer

    def perform_create(self, serializer):
        serializer.save()

class TherapyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Therapy.objects.order_by('name')
    serializer_class = TherapySerializer

    def perform_create(self, serializer):
        serializer.save()


class SubTherapyView(generics.ListCreateAPIView):
    queryset = SubTherapy.objects.order_by('name')
    serializer_class = SubTherapySerializer

    def perform_create(self, serializer):
        serializer.save()

class SubTherapyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTherapy.objects.order_by('name')
    serializer_class = SubTherapySerializer

    def perform_create(self, serializer):
        serializer.save()

class AdvertisementView(generics.ListCreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def perform_create(self, serializer):
        serializer.save()