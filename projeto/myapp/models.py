from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=10)
    meta = models.IntegerField()

class Vendas(models.Model):
    id_usuario = models.IntegerField()
    valor = models.IntegerField()