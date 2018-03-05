from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import SchemeSerializer, MapSerializer, BuildingSerializer, FloorSerializer, RoomSerializer, \
    CoordinateSerializer
from .models import Scheme, Map, Building, Floor, Room
from rest_framework.permissions import IsAuthenticated


class CreateSchemeView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailSchemeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer


class CreateMapView(generics.ListCreateAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailMapView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class CreateBuildingView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailBuildingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class CreateFloorView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailFloorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer


class CreateRoomView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('subtherapies__name', 'number')

    def perform_create(self, serializer):
        serializer.save()


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class FindPathView(APIView):
    def get(self, request, format=None):

        # parse query
        from_floor_id = request.query_params.get('floor')
        to_room_id = request.query_params.get('room')

        # get the room which's looking for
        room = Room.objects.get(pk=to_room_id)
        room_coordinate_serializer = CoordinateSerializer(room.coordinate)

        # get current floor
        current_floor = Floor.objects.get(pk=from_floor_id)
        current_floor_serializer = FloorSerializer(current_floor)

        # get a floor where is room located
        other_floor = Floor.objects.get(pk=room.floor.id)
        other_floor_serializer = FloorSerializer(other_floor)

        # same buildings
        if (current_floor.building.id == other_floor.building.id):
            if (current_floor.number - other_floor.number == 0):
                return Response([{
                    'case': 0,
                    'currentFloor': current_floor_serializer.data,
                    'roomCoordinate': room_coordinate_serializer.data
                }])
            else:
                return Response([{
                    'case': 1,
                    'currentFloor': current_floor_serializer.data,
                    'otherFloor': other_floor_serializer.data,
                    'roomCoordinate': room_coordinate_serializer.data
                }])
        # different buildings
        else:
            print('1')
            current_building = Building.objects.get(pk=current_floor.building.id)
            current_building_serializer = BuildingSerializer(current_building)
            other_building = Building.objects.get(pk=other_floor.building.id)
            other_building_serializer = BuildingSerializer(other_building)
            # building with passageway
            if current_building.isPassageway:
                print('2')
                # from buildings
                current_floor_is_contain_passageway_to_other_floor = Floor.objects.filter(
                    passageway__toBuildingId=other_floor.building.id, building=current_floor.building.id)
                if (not current_floor_is_contain_passageway_to_other_floor):
                    # work for building woth one passageway, need to fix in the future

                    current_building_floor_with_passageway = \
                        Floor.objects.filter(passageway__toBuildingId=current_floor.building.id)[0]
                    current_building_floor_with_passageway_serializer = FloorSerializer(
                        current_building_floor_with_passageway)

                    other_building_floor_with_passageway = \
                        Floor.objects.filter(passageway__toBuildingId=other_floor.building.id,
                                             building=current_building_floor_with_passageway.building.id)[0]
                    other_building_floor_with_passageway_serializer = FloorSerializer(
                        other_building_floor_with_passageway)

                    return Response([{
                        'case': 10,
                        'currentFloor': current_floor_serializer.data,
                        'currentPassagewayFloor': current_building_floor_with_passageway_serializer.data,
                        'otherPassagewayFloor': other_building_floor_with_passageway_serializer.data,
                        'otherFloor': other_floor_serializer.data,
                        'roomCoordinate': room_coordinate_serializer.data
                    }])
                    # case 11 - current floor without passageaway
                    # case 12 - other floor without passageaway
                # buildings near
                if (current_floor.number == other_floor.number) and current_floor.passageway and (
                        current_floor.passageway.toBuildingId == other_floor.building.id) and (
                        other_floor.passageway.toBuildingId == current_floor.building.id):
                    return Response([{
                        'case': 2,
                        'currentFloor': current_floor_serializer.data,
                        'otherFloor': other_floor_serializer.data,
                        'roomCoordinate': room_coordinate_serializer.data
                    }])
                elif (current_floor.number == other_floor.number):
                    print('2-1')
                    current_building_floor_with_passageway = \
                        Floor.objects.filter(passageway__toBuildingId=other_floor.building.id,
                                             building=current_floor.building.id)[0]
                    current_building_floor_with_passageway_serializer = FloorSerializer(
                        current_building_floor_with_passageway)
                    other_building_floor_with_passageway = \
                        Floor.objects.filter(passageway__toBuildingId=current_floor.building.id,
                                             building=other_floor.building.id)[0]
                    other_building_floor_with_passageway_serializer = FloorSerializer(
                        other_building_floor_with_passageway)

                    return Response([{
                        'case': 5,
                        'currentFloor': current_floor_serializer.data,
                        'currentPassagewayFloor': current_building_floor_with_passageway_serializer.data,
                        'otherFloor': other_floor_serializer.data,
                        'otherPassagewayFloor': other_building_floor_with_passageway_serializer.data,
                        'roomCoordinate': room_coordinate_serializer.data
                    }])

                elif (current_floor.number != other_floor.number):
                    if (current_floor.passageway.toBuildingId != other_floor.building.id) and (
                            other_floor.passageway == current_floor.building.id):
                        print("case 3")
                        current_building_floor_with_passageway = \
                            Floor.objects.filter(passageway__toBuildingId=other_floor.building.id,
                                                 building=current_floor.building.id)[0]
                        current_building_floor_with_passageway_serializer = FloorSerializer(
                            current_building_floor_with_passageway)

                        return Response([{
                            'case': 3,
                            'currentFloor': current_floor_serializer.data,
                            'currentPassagewayFloor': current_building_floor_with_passageway_serializer.data,
                            'otherFloor': other_floor_serializer.data,
                            'roomCoordinate': room_coordinate_serializer.data
                        }])
                    elif (current_floor.passageway.toBuildingId == other_floor.building.id):
                        other_building_floor_with_passageway = \
                            Floor.objects.filter(passageway__toBuildingId=current_floor.building.id,
                                                 building=other_floor.building.id)[0]
                        other_building_floor_with_passageway_serializer = FloorSerializer(
                            other_building_floor_with_passageway)
                        print("case 4")
                        return Response([{
                            'case': 4,
                            'currentFloor': current_floor_serializer.data,
                            'otherPassagewayFloor': other_building_floor_with_passageway_serializer.data,
                            'otherFloor': other_floor_serializer.data,
                            'roomCoordinate': room_coordinate_serializer.data
                        }])

                    if (current_floor.passageway.toBuildingId != other_floor.building.id) and (
                            not other_floor.passageway):
                        print("case 5")
                        current_building_floor_with_passageway = \
                            Floor.objects.filter(passageway__toBuildingId=other_floor.building.id,
                                                 building=current_floor.building.id)[0]
                        current_building_floor_with_passageway_serializer = FloorSerializer(
                            current_building_floor_with_passageway)
                        other_building_floor_with_passageway = \
                            Floor.objects.filter(passageway__toBuildingId=current_floor.building.id,
                                                 building=other_floor.building.id)[0]
                        other_building_floor_with_passageway_serializer = FloorSerializer(
                            other_building_floor_with_passageway)

                        return Response([{
                            'case': 5,
                            'currentFloor': current_floor_serializer.data,
                            'currentPassagewayFloor': current_building_floor_with_passageway_serializer.data,
                            'otherFloor': other_floor_serializer.data,
                            'otherPassagewayFloor': other_building_floor_with_passageway_serializer.data,
                            'roomCoordinate': room_coordinate_serializer.data
                        }])
                    if (current_floor.passageway.toBuildingId != other_floor.building.id) and other_floor.passageway:
                        print("case 11")
                        current_building_floor_with_passageway = \
                        Floor.objects.filter(passageway__toBuildingId=other_floor.building.id,
                                             building=current_floor.building.id)[0]
                        current_building_floor_with_passageway_serializer = FloorSerializer(
                            current_building_floor_with_passageway)

                        return Response([{
                            'case': 11,
                            'currentFloor': current_floor_serializer.data,
                            'currentPassagewayFloor': current_building_floor_with_passageway_serializer.data,
                            'otherFloor': other_floor_serializer.data,
                            # 'otherPassagewayFloor': other_building_floor_with_passageway_serializer.data,
                            'roomCoordinate': room_coordinate_serializer.data
                        }])

            # building without passageway
            # else:
            #     scheme = Scheme.objects.get(current_building.scheme)
            #     map = Map.objects.get(scheme.map)
            #     map_serizlizer = MapSerializer(map)
            #
            #     if (current_floor.number == 1) and (other_floor.number == 1):
            #         return Response([{
            #             'case': 6,
            #             'currentFloor': current_floor_serializer.data,
            #             'otherFloor': other_floor_serializer.data,
            #             'roomCoordinate': room_coordinate_serializer.data,
            #             'current_building': current_building_serializer.data,
            #             'other_building': other_building_serializer.data,
            #             'map': map_serizlizer.data
            #         }])
            #     elif (current_floor.number > 1) and (other_floor.number == 1):
            #         current_floor_first = Floor.objects.get(building=current_building, number=1)
            #         current_floor_first_serializer = FloorSerializer(current_floor_first)
            #         return Response([{
            #             'case': 7,
            #             'currentFloor': current_floor_serializer.data,
            #             'currentFloorFirst': current_floor_first_serializer.data,
            #             'otherFloor': other_floor_serializer.data,
            #             'roomCoordinate': room_coordinate_serializer.data,
            #             'current_building': current_building_serializer.data,
            #             'other_building': other_building_serializer.data,
            #             'map': map_serizlizer.data
            #         }])
            #     elif (current_floor.number == 1) and (other_floor.number > 1):
            #         other_floor_first = Floor.objects.get(building=other_building, number=1)
            #         other_floor_first_serializer = FloorSerializer(other_floor_first)
            #         return Response([{
            #             'case': 8,
            #             'currentFloor': current_floor_serializer.data,
            #             'otherFloor': other_floor_serializer.data,
            #             'otherFloorFirst': other_floor_first_serializer.data,
            #             'roomCoordinate': room_coordinate_serializer.data,
            #             'current_building': current_building_serializer.data,
            #             'other_building': other_building_serializer.data,
            #             'map': map_serizlizer.data
            #         }])
            #     elif (current_floor.number > 1) and (other_floor.number > 1):
            #         current_floor_first = Floor.objects.get(building=current_building, number=1)
            #         current_floor_first_serializer = FloorSerializer(current_floor_first)
            #         other_floor_first = Floor.objects.get(building=other_building, number=1)
            #         other_floor_first_serializer = FloorSerializer(other_floor_first)
            #         return Response([{
            #             'case': 9,
            #             'currentFloor': current_floor_serializer.data,
            #             'currentFloorFirst': current_floor_first_serializer.data,
            #             'otherFloor': other_floor_serializer.data,
            #             'otherFloorFirst': other_floor_first_serializer.data,
            #             'roomCoordinate': room_coordinate_serializer.data,
            #             'current_building': current_building_serializer.data,
            #             'other_building': other_building_serializer.data,
            #             'map': map_serizlizer.data
            #         }])
