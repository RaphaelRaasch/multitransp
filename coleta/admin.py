from django.contrib import admin
from .models import Coleta


@admin.register(Coleta)
class ColetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'peso', 'logradouro')
    list_display_links =('produto',)
    list_filter=('produto',)
