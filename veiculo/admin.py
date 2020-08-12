from django.contrib import admin
from .models import Truck, Reboque, Conjunto


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'placa')
    list_display_links = ('modelo',)


@admin.register(Reboque)
class ReboqueAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'placa')
    list_display_links = ('modelo',)


@admin.register(Conjunto)
class ConjuntoAdmin(admin.ModelAdmin):
    list_display = ('name','truck','reboque')
    list_display_links = ('name',)
    search_fields = ('name',)