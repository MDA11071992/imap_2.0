#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import *


# content
class AdminImageServices(admin.TabularInline):
    model = ImageService
    extra = 0
    readonly_fields = ('image_tag',)


@admin.register(Service)
class AdminServices(admin.ModelAdmin):
    inlines = [AdminImageServices]
    ordering = ['name']
    search_fields = ['name']


# room
class AdminImageRoom(admin.TabularInline):
    model = ImageRoom
    extra = 0
    readonly_fields = ('image_tag',)


class AdminVoucherInline(admin.TabularInline):
    model = Voucher
    extra = 0


class AdminPriceRoom(admin.TabularInline):
    model = PriceRoom
    extra = 0


@admin.register(Currency)
class AdminCurrency(admin.ModelAdmin):
    inlines = [AdminPriceRoom]
    list_display = ('name', 'voucher',)
    ordering = ['name']
    list_filter = ('voucher__room',)


@admin.register(Room)
class AdminRoom(admin.ModelAdmin):
    inlines = [AdminImageRoom, AdminVoucherInline]
    ordering = ['name']


# therapy
class AdminImageTherapy(admin.TabularInline):
    model = ImageTherapy
    extra = 0
    readonly_fields = ('image_tag',)


@admin.register(SubTherapy)
class AdminTherapy(admin.ModelAdmin):
    inlines = [AdminImageTherapy]
    list_display = ('name', 'therapy',)
    list_filter = ('room__floor',)
    search_fields = ['name']
    extra = 0
    ordering = ['name']
    # formfield_overrides = {
    #     models.TextField: {'widget': Textarea(attrs={'rows': 30, 'cols': 200})},
    # }


@admin.register(Therapy)
class AdminPackageTherapy(admin.ModelAdmin):
    ordering = ['name']


@admin.register(Advertisement)
class AdminAdvertisement(admin.ModelAdmin):
    ordering = ['video']
