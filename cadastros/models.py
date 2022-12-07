from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=100, default="")
    curso = models.CharField(max_length=40, default="")
    periodo = models.IntegerField(blank=False, default=00)
    horas_disponiveis = models.IntegerField(blank=False, default=00)

    def __str__(self):
        return self.nome
