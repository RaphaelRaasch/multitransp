from django.db import models


class Truck(models.Model):
    modelo = models.CharField('Modelo', max_length=50)
    placa = models.CharField('Placa', max_length=7)

    def __str__(self):
        return self.placa


class Reboque(models.Model):
    modelo = models.CharField('Modelo', max_length=50)
    placa = models.CharField('Placa', max_length=7)

    def __str__(self):
        return self.placa


class Conjunto(models.Model):
    name = models.CharField('Name', max_length=150)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    reboque = models.ForeignKey(Reboque, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
