from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.utils import timezone


class Categoria (models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Contato (models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete= DO_NOTHING)

    def __str__(self):
        return self.nome

    