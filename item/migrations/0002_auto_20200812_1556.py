# Generated by Django 2.2.9 on 2020-08-12 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='descricao',
            field=models.CharField(max_length=50, verbose_name='Descrição'),
        ),
    ]
