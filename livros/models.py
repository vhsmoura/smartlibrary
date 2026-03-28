from django.db import models
from django.utils import timezone
from datetime import timedelta

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='livros/')
    aluno = models.CharField(max_length=100, blank=True)
    data_emprestimo = models.DateField(null=True, blank=True)
    data_devolucao = models.DateField(null=True, blank=True)

    def dias_restantes(self):
        if self.data_devolucao:
            return max(0, (self.data_devolucao - timezone.now().date()).days)
        return None

