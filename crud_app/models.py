from django.db import models

class Usuario(models.Model):
    # todos os campos são obrigatórios.
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    clcb = models.IntegerField()
    senha = models.CharField(max_length=255)
    data_cadastro = models.DateTimeField(auto_now_add=True) # adicionado automaticamente.

    def __str__(self):
        return self.nome

class Incendio(models.Model):
    # todos os campos são obrigatórios.
    # cada alerta de incêndio obrigatoriamente deve ter um usuário associado. somente usuários cadastrados poderão adicionar alertas de incêndio. usuários deletados terão seus alertas apagados também.
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    local = models.CharField(max_length=255)
    GRAVIDADE_CHOICES = [
        ('grave', 'Grave'),
        ('medio', 'Médio'),
        ('baixo', 'Baixo'),
    ]
    gravidade = models.CharField(max_length=10, choices=GRAVIDADE_CHOICES)

    def __str__(self):
        return self.local
