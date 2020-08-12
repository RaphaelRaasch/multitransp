from rest_framework.viewsets import ModelViewSet
from .models import Coleta
from .serializers import ColetaSerializer

class ColetaViewSet(ModelViewSet):
    queryset = Coleta.objects.all()
    serializer_class = ColetaSerializer