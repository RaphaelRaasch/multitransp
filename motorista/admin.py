from django.contrib import admin
from .models import Motorista


@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'cnh')
    list_display_links = ('name',)
