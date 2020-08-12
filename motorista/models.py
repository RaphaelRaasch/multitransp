from django.db import models


class Motorista(models.Model):
    name = models.CharField('Name', max_length=155)
    cpf = models.CharField('CPF', max_length=11)
    cnh = models.CharField('CNH', max_length=11)

    def __str__(self):
        return self.name
