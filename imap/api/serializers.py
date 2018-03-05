from rest_framework import serializers
from .models import Scheme, Building, Map, Coordinate, Room, Floor, Terminal, Passageway
from info.models import Service, SubTherapy
from info.serializers import SubTherapySerializer
from PIL import Image
import pickle
import os
from imap.settings import MEDIA_ROOT


class CoordinateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Coordinate
        fields = '__all__'


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'


class TerminalSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    coordinate = CoordinateSerializer()

    class Meta:
        model = Terminal
        fields = '__all__'


class PassagewaySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    coordinate = CoordinateSerializer()

    class Meta:
        model = Passageway
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    coordinate = CoordinateSerializer()
    subtherapies = SubTherapySerializer(many=True, required=False)

    class Meta:
        model = Room
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    entrance = CoordinateSerializer()
    terminal = TerminalSerializer(required=False, allow_null=True)
    passageway = PassagewaySerializer(required=False, allow_null=True)
    rooms = RoomSerializer(many=True)

    class Meta:
        model = Floor
        fields = '__all__'

    def create(self, validated_data):
        # create entrance coordinate
        entrance_coordinate = validated_data.get('entrance')
        entrance_coordinate_obj = Coordinate.objects.create(**entrance_coordinate)

        # create terminal coordinate
        terminal = validated_data.get('terminal')

        if terminal:
            terminal_coordinate = terminal.get('coordinate')
            terminal_coordinate_obj = Coordinate.objects.create(**terminal_coordinate)
            terminal_obj = Terminal.objects.create(coordinate=terminal_coordinate_obj)
        else:
            terminal_obj = None

        # create passageway coordinate
        passageway = validated_data.get('passageway')

        if passageway:
            passageway_coordinate = passageway.pop('coordinate')
            passageway_coordinate_obj = Coordinate.objects.create(**passageway_coordinate)
            passageway_obj = Passageway.objects.create(coordinate=passageway_coordinate_obj, **passageway)
        else:
            passageway_obj = None

        # create floor entity
        number = validated_data.get('number')
        building = validated_data.get('building')
        map = validated_data.get('map')
        floor = Floor.objects.create(number=number, building=building, map=map, entrance=entrance_coordinate_obj,
                                     terminal=terminal_obj, passageway=passageway_obj)

        # get rooms
        rooms = validated_data.pop('rooms')

        # create rooms
        for room in rooms:
            data_coordinate = room.pop('coordinate')
            room_coordinate = Coordinate.objects.create(**data_coordinate)
            Room.objects.create(floor=floor, coordinate=room_coordinate, **room)

        return floor

    def update(self, instance, validated_data):
        rooms_data = validated_data.pop('rooms')
        terminal_data = validated_data.get('terminal')
        passageway_data = validated_data.get('passageway')
        entrance_data = validated_data.pop('entrance')

        rooms = list((instance.rooms).all())

        # Perform scheme update.
        instance.number = validated_data.get('number', instance.number)
        instance.map = validated_data.get('map', instance.map)

        # entrance
        entrance_coordinate_id = entrance_data.get('id')
        coordinate_entrance = Coordinate.objects.get(pk=entrance_coordinate_id)
        coordinate_entrance.x = entrance_data.get('x', coordinate_entrance.x)
        coordinate_entrance.y = entrance_data.get('y', coordinate_entrance.y)
        coordinate_entrance.save()

        if (passageway_data):
            coordinate_passageway = passageway_data.get('coordinate')
            if not passageway_data.get('id'):
                passageway_coordinate_new = Coordinate.objects.create(**coordinate_passageway)
                passageway_obj = Passageway.objects.create(coordinate=passageway_coordinate_new,
                                                           toBuildingId=passageway_data.get('toBuildingId'))
                instance.passageway = passageway_obj
            else:
                instance_passageway = Passageway.objects.get(pk=passageway_data.get('id'))
                instance_passageway.toBuildingId = passageway_data.get('toBuildingId', instance_passageway.toBuildingId)
                instance_passageway.save()
                if (coordinate_passageway.get('id')):
                    coordinate_passageway_obj = Coordinate.objects.get(pk=coordinate_passageway.get('id'))
                    coordinate_passageway_obj.x = coordinate_passageway.get('x', coordinate_passageway_obj.x)
                    coordinate_passageway_obj.y = coordinate_passageway.get('y', coordinate_passageway_obj.y)
                    coordinate_passageway_obj.save()
                else:
                    passageway_coordinate_new = Coordinate.objects.create(**coordinate_passageway)
                    passageway_obj = Passageway.objects.create(coordinate=passageway_coordinate_new,
                                                               toBuildingId=passageway_data.get('toBuildingId'))
                    instance.passageway = passageway_obj
        else:
            instance.passageway = None

        if (terminal_data):
            coordinate_terminal = terminal_data.get('coordinate')
            if (coordinate_terminal.get('id')):
                coordinate_terminal_obj = Coordinate.objects.get(pk=coordinate_terminal.get('id'))
                coordinate_terminal_obj.x = coordinate_terminal.get('x', coordinate_terminal_obj.x)
                coordinate_terminal_obj.y = coordinate_terminal.get('y', coordinate_terminal_obj.y)
                coordinate_terminal_obj.save()
            else:
                terminal_coordinate_new = Coordinate.objects.create(**coordinate_terminal)
                terminal_obj = Terminal.objects.create(coordinate=terminal_coordinate_new)
                instance.terminal = terminal_obj
        else:
            instance.terminal = None

        instance.save()

        # Perform creations and updates rooms.
        for room_data in rooms_data:
            if room_data.get('id'):
                for room in rooms:
                    if room.id == room_data.get('id'):
                        room.number = room_data.get('number', room.number)

                        data_coordinate = room_data.pop('coordinate')
                        coordinate_id = data_coordinate.get('id')
                        if (coordinate_id):
                            coordinate_instance = Coordinate.objects.get(pk=coordinate_id)
                            coordinate_instance.x = data_coordinate.get('x', coordinate_instance.x)
                            coordinate_instance.y = data_coordinate.get('y', coordinate_instance.y)
                            coordinate_instance.save()
                        else:
                            room_coordinate = Coordinate.objects.create(**data_coordinate)
                            room.coordinate = room_coordinate

                        room.save()
                        rooms.remove(room)
            else:
                data_coordinate = room_data.pop('coordinate')
                room_coordinate = Coordinate.objects.create(**data_coordinate)
                Room.objects.create(floor=instance, coordinate=room_coordinate, **room_data)

        # Perform deletions tracks.
        for room_to_delete in rooms:
            room_to_delete.delete()

        return instance


class FloorListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Floor
        fields = ('id', 'number')


class BuildingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    coordinate = CoordinateSerializer()
    floors = FloorListSerializer(many=True, required=False)

    class Meta:
        model = Building
        fields = ('__all__')


class SchemeSerializer(serializers.ModelSerializer):
    buildings = BuildingSerializer(many=True)

    class Meta:
        model = Scheme
        fields = ('__all__')

    def create(self, validated_data):
        # get buildings
        buildings = validated_data.pop('buildings')

        # create scheme entity
        name = validated_data.get('name')
        map = validated_data.get('map')
        scheme = Scheme.objects.create(name=name, map=map)

        # create buildings
        for building in buildings:
            data_coordinate = building.pop('coordinate')
            building_coordinate = Coordinate.objects.create(**data_coordinate)
            Building.objects.create(scheme=scheme, coordinate=building_coordinate, **building)

        return scheme

    def update(self, instance, validated_data):
        buildings_data = validated_data.pop('buildings')
        buildings = list((instance.buildings).all())

        # Perform scheme update.
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        # Perform creations and updates buildings.
        for building_data in buildings_data:
            if building_data.get('id'):
                for building in buildings:
                    if building.id == building_data.get('id'):
                        building.name = building_data.get('name', building.name)
                        building.isPassageway = building_data.get('isPassageway', building.isPassageway)

                        data_coordinate = building_data.pop('coordinate')
                        coordinate_id = data_coordinate.get('id')
                        if (coordinate_id):
                            coordinate_instance = Coordinate.objects.get(pk=coordinate_id)
                            coordinate_instance.x = data_coordinate.get('x', coordinate_instance.x)
                            coordinate_instance.y = data_coordinate.get('y', coordinate_instance.y)
                            coordinate_instance.save()
                        else:
                            building_coordinate = Coordinate.objects.create(**data_coordinate)
                            building.coordinate = building_coordinate

                        building.save()
                        buildings.remove(building)
            else:
                print('create')
                data_coordinate = building_data.pop('coordinate')
                building_coordinate = Coordinate.objects.create(**data_coordinate)
                Building.objects.create(scheme=instance, coordinate=building_coordinate, **building_data)

        # Perform delete buildings.
        for building_to_delete in buildings:
            building_to_delete.delete()

        return instance
