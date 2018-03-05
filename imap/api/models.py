from django.db import models
from django_resized import ResizedImageField


# from info.models import SubTherapy

class Coordinate(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return "{}".format(self.id)


class Map(models.Model):
    image = ResizedImageField(size=[1920, 1080], quality=100, upload_to='maps')

    def __str__(self):
        return "{}".format(self.id)


class Terminal(models.Model):
    coordinate = models.OneToOneField(Coordinate, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.id)


class Passageway(models.Model):
    coordinate = models.OneToOneField(Coordinate, on_delete=models.CASCADE)
    toBuildingId = models.IntegerField(default=None)

    def __str__(self):
        return "{}".format(self.id)


class Scheme(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    map = models.OneToOneField(Map, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)


class Building(models.Model):
    name = models.CharField(max_length=255)
    isPassageway = models.BooleanField(default=False)
    scheme = models.ForeignKey(Scheme, related_name='buildings', blank=True, null=True, on_delete=models.CASCADE)
    coordinate = models.OneToOneField(Coordinate, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)


class Floor(models.Model):
    number = models.IntegerField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='floors')
    map = models.OneToOneField(Map, on_delete=models.CASCADE)
    entrance = models.OneToOneField(Coordinate, on_delete=models.CASCADE)
    terminal = models.OneToOneField(Terminal, on_delete=models.CASCADE, blank=True, null=True)
    passageway = models.OneToOneField(Passageway, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "Этаж: {0}, Здание: {1}".format(self.number, self.building.name)


class Room(models.Model):
    number = models.CharField(max_length=255)
    floor = models.ForeignKey(Floor, related_name='rooms', blank=True, null=True, on_delete=models.CASCADE)
    coordinate = models.OneToOneField(Coordinate, on_delete=models.CASCADE)

    def __str__(self):
        return "Здание: {0}, Этаж: {1}, Комната: {2}".format(self.floor.building, self.floor, self.number)
