from rest_framework.serializers import ModelSerializer
from .models import Coleta


class ColetaSerializer(ModelSerializer):
    class Meta:
        model = Coleta
        fields = ['id', 'produto', 'peso', 'logradouro', 'bairro', 'municipio', 'estado', 'numero', 'local_descricao']
