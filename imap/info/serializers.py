from rest_framework.serializers import ModelSerializer
from .models import Service, ImageService, Room, ImageRoom, Therapy, SubTherapy, ImageTherapy, PriceRoom, Currency, \
    Voucher, Advertisement


# service
class ServiceImageSerializer(ModelSerializer):
    class Meta:
        model = ImageService
        fields = '__all__'


class ServiceSerializer(ModelSerializer):
    images = ServiceImageSerializer(many=True)

    class Meta:
        model = Service
        fields = '__all__'


class ServiceNameSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name')


# room
class RoomImageSerializer(ModelSerializer):
    class Meta:
        model = ImageRoom
        fields = '__all__'


class PriceRoomSerializer(ModelSerializer):
    class Meta:
        model = PriceRoom
        fields = '__all__'


class CurrencySerializer(ModelSerializer):
    price_type = PriceRoomSerializer(many=True)

    class Meta:
        model = Currency
        fields = '__all__'


class VoucherSerializer(ModelSerializer):
    currency = CurrencySerializer(many=True)

    class Meta:
        model = Voucher
        fields = '__all__'


class RoomSerializer(ModelSerializer):
    images = RoomImageSerializer(many=True)
    voucher = VoucherSerializer(many=True)

    class Meta:
        model = Room
        fields = '__all__'


class RoomNameSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name')


# therapy
class ImageTherapySerializer(ModelSerializer):
    class Meta:
        model = ImageTherapy
        fields = '__all__'


class SubTherapySerializer(ModelSerializer):
    images = ImageTherapySerializer(many=True)

    class Meta:
        model = SubTherapy
        fields = '__all__'


class SubTherapyNameSerializer(ModelSerializer):
    class Meta:
        model = SubTherapy
        fields = ('id', 'name')


class TherapySerializer(ModelSerializer):
    therapy = SubTherapySerializer(many=True)

    class Meta:
        model = Therapy
        fields = '__all__'


class TherapyNameSerializer(ModelSerializer):
    therapy = SubTherapyNameSerializer(many=True)

    class Meta:
        model = Therapy
        fields = '__all__'


class AdvertisementSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'
