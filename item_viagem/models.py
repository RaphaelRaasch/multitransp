from django.db import models
from viagem.models import Viagem
from item.models import Item


class ItemViagem(models.Model):
    viagem = models.ForeignKey(Viagem, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.IntegerField('Quantidade')
    valor_unitario = models.DecimalField('Valor unitario', max_digits=10, decimal_places=2)
    valor_total = models.DecimalField('Valor Toral', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.viagem
