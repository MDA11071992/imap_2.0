#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from api.models import Room as Api_room
from django.utils.safestring import mark_safe


# services
class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    room = models.OneToOneField(Api_room, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Комната')

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return "{}".format(self.name)


class ImageService(models.Model):
    image = models.ImageField(upload_to='content/', verbose_name='Изображение')
    service = models.ForeignKey(Service, related_name='images', blank=True, null=True, on_delete=models.CASCADE)

    def image_tag(self):
        return mark_safe('<img src="%s" height="150" />' % self.image.url)

    image_tag.short_description = 'image'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return "{}".format(self.id)


# room
class Room(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'

    def __str__(self):
        return "{}".format(self.name)


class ImageRoom(models.Model):
    image = models.ImageField(upload_to='room/', verbose_name='Изображение')
    room = models.ForeignKey(Room, related_name='images', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Комната')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return "{}".format(self.id)

    def image_tag(self):
        return mark_safe('<img src="%s" height="150" />' % self.image.url)

    image_tag.short_description = 'image'
    image_tag.allow_tags = True


class Voucher(models.Model):
    room = models.ForeignKey(Room, related_name='voucher', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Комната')
    name = models.CharField(max_length=200, verbose_name='Название')

    class Meta:
        verbose_name = 'Путевка'
        verbose_name_plural = 'Путевка'

    def __str__(self):
        return "Путевка: {0}, Комната: {1}".format(self.name, self.room)


class Currency(models.Model):
    voucher = models.ForeignKey(Voucher, related_name='currency', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Путевка')
    name = models.CharField(max_length=200, verbose_name='Название')

    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайс'

    def __str__(self):
        return "{}".format(self.name)


class PriceRoom(models.Model):
    currency_type = models.ForeignKey(Currency, related_name='price_type', blank=True, null=True,
                                      on_delete=models.CASCADE,)
    during = models.CharField(max_length=200, blank=True, null=True, verbose_name='Даты')
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=True, verbose_name = 'Цена за сутки')

    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайс'

    def __str__(self):
        return "{}".format(self.during)


# therapy
class Therapy(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')

    class Meta:
        verbose_name = 'Лечение'
        verbose_name_plural = 'Лечение'

    def __str__(self):
        return "{}".format(self.name)


class SubTherapy(models.Model):
    therapy = models.ForeignKey(Therapy, related_name='therapy', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Терапия')
    name = models.CharField(max_length=200, help_text='Название', verbose_name='Название')
    description = models.TextField(help_text='Описание', verbose_name='Описание')
    #movie = models.FileField(upload_to='therapy/', blank=True, null=True,)
    room = models.ForeignKey(Api_room, related_name='subtherapies', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Комната')

    class Meta:
        verbose_name = 'Каталог лечения'
        verbose_name_plural = 'Каталоги лечения'

    def __str__(self):
        return "{}".format(self.id)


class ImageTherapy(models.Model):
    image = models.ImageField(upload_to='therapy/', verbose_name='Изображение')
    subtherapy = models.ForeignKey(SubTherapy, related_name='images', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return "{}".format(self.id)

    def image_tag(self):
        return mark_safe('<img src="%s" height="150" />' % self.image.url)

    image_tag.short_description = 'image'
    image_tag.allow_tags = True


class Advertisement(models.Model):
    video = models.FileField(upload_to='advertisement/')

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Реклама'

    def __str__(self):
        return "{}".format(self.video)

