from django.contrib import admin
from .models import Viagem


@admin.register(Viagem)
class ViagemAdmin(admin.ModelAdmin):
    list_display = ('alias', 'motorista', 'veiculo', 'origem', 'destino')
    list_display_links = ('alias', 'motorista')
