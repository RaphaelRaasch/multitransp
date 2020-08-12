# Generated by Django 2.2.9 on 2020-08-11 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Name')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('cnh', models.CharField(max_length=11, verbose_name='CNH')),
            ],
        ),
    ]
