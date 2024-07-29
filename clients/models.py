from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.nome

class Carro(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    carro = models.CharField(max_length=255)
    placa = models.CharField(max_length=8)
    ano = models.IntegerField()
    lavagens = models.IntegerField(default=0)
    consertos = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.carro