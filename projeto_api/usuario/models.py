from django.db import models

class Modalidade(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.CharField(max_length=100) 
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    modalidade = models.ForeignKey(Modalidade, related_name='usuarios', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='usuario/', blank=True, null=True)
    def __str__(self):
        return self.nome
