from django.db import models
from motorista.models import Motorista
from veiculo.models import Reboque


class Viagem(models.Model):
    alias = models.CharField('Alias', max_length=50)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Reboque, on_delete=models.CASCADE)
    inicio = models.DateTimeField('Data e hora do inicio', auto_now_add=False)
    origem = models.CharField('Origem', max_length=155)
    destino = models.CharField('Destino', max_length=155)
    obs = models.TextField('Observações')

    def __str__(self):
        return f'{self.alias}'
