from django.db import models


class Coleta(models.Model):
    produto = models.CharField('Produto', max_length=155)
    peso = models.DecimalField('Peso', max_digits=6,decimal_places=2)
    logradouro = models.CharField('Logradouro', max_length=155)
    bairro = models.CharField('Bairro', max_length=155)
    municipio = models.CharField('Municipio', max_length=155)
    estado = models.CharField('Estado', max_length=155)
    numero = models.IntegerField('Numero')
    local_descricao = models.CharField('Descrição do local', max_length=155)



