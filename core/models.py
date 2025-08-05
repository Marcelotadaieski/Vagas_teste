from django.db import models
from datetime import date

# Create your models here.

STATUS_VAGA = (
    ('aberta','Aberta'),
    ('fechada', 'Fechada'),
)

class Vaga(models.Model):
    titulo = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_VAGA, default='aberta')
    data_criacao = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-data_criacao']

    def __str__(self):
        return self.titulo
    
class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    vagas = models.ManyToManyField(Vaga, related_name='candidatos', blank=True)

    def idade(self):
        hoje = date.today()
        nasc = self.data_nascimento
        anos = hoje.year - nasc.year
        # se ainda não fez aniversário neste ano, subtrai 1
        if (hoje.month, hoje.day) < (nasc.month, nasc.day):
            anos -= 1
        # garante que sempre retornamos um inteiro
        return anos
    
    def __str__(self):
        return self.nome