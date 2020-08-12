from django.db import models


class Item(models.Model):
    ITEM_CHOICES = (
        ('D', 'Debito'),
        ('R', 'Receita')
    )
    tipo = models.CharField('Tipo', max_length=1, choices=ITEM_CHOICES)
    descricao = models.CharField('Descrição', max_length=50)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.descricao} {self.tipo}'
