from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.nome


class Noticia(models.Model):
    titulo = models.CharField(max_length=150, blank=False)
    texto = models.TextField(blank=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    @property
    def nome_autor(self):
        return self.autor.nome
