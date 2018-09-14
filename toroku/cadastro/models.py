from django.db import models

SEXO_CHOICES = (
    (0, 'Não Informado'),
    (1, 'Homem'),
    (2, 'Mulher'),
)

# Create your models here.
class Visitante(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    cpf = models.CharField('CPF',max_length=50)
    aniversario = models.DateField('aniversario')
    sexo = models.PositiveSmallIntegerField(choices=SEXO_CHOICES, default=0)
    CodigoBarra = models.CharField('Crachá',max_length=50)
