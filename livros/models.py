from django.db import models
from django.utils import timezone
from django.core.files import File

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    aluno = models.CharField(max_length=100, blank=True, null=True)
    data_devolucao = models.DateField(null=True, blank=True)
    imagem = models.ImageField(upload_to='livros/', blank=True, null=True)  # ← null=True

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Calcula data devolução automática
        if self.aluno and not self.data_devolucao:
            self.data_devolucao = timezone.now().date() + timezone.timedelta(days=80)
            super().save(update_fields=['data_devolucao'])

    def dias_restantes(self):
        if self.data_devolucao and self.data_devolucao > timezone.now().date():
            return (self.data_devolucao - timezone.now().date()).days
        return 0

    def __str__(self):
        return self.titulo