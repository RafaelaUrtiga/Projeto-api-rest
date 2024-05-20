from django.db import models

class Task (models.Model):
    titulo = models.CharField(max_length=255)
    prazo = models.DateField(null=True, blank=True)
    descricao = models.TextField(blank=True)
    finalizada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo + ': ' + self.descricao
    

