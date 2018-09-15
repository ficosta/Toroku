from django.db import models

SEXO_CHOICES = (
    (0, 'Não Informado'),
    (1, 'Homem'),
    (2, 'Mulher'),
)
TIPO_CHOICES = (
    (0, 'Visitante'),
    (1, 'Lojista'),
)

# Create your models here.
class Visitante(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    email = models.EmailField('Email')
    telefone = models.CharField(max_length=15,help_text='(xx)xxxxx-xxxx', blank=True)
    documento = models.CharField('CPF/CNPJ',max_length=50)
    aniversario = models.DateField('aniversario', blank=True)
    sexo = models.PositiveSmallIntegerField(choices=SEXO_CHOICES, default=0)
    tipo = models.PositiveSmallIntegerField(choices=TIPO_CHOICES, default=0)
    CodigoBarra = models.CharField('Crachá',max_length=50, blank=True)
