from django.test import TestCase
from portal_noticias.models import Autor, Noticia
from api import settings
import os


class AutorTestClass(TestCase):
    """
    Responsável por testar a estrutura de dados.
    """
    @classmethod
    def setUpTestData(cls):
        settings.DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
            }
        }
        Autor.objects.create(nome="Ferdinando Americo")

    def test_campo_nome(self):
        autor = Autor.objects.get(id=1)
        campo_nome = autor._meta.get_field('nome').verbose_name
        self.assertEquals(campo_nome, 'nome')

    def test_campo_nome_max_length(self):
        autor = Autor.objects.get(id=1)
        max_length = autor._meta.get_field('nome').max_length
        self.assertEquals(max_length, 100)


class NoticiaTestClass(TestCase):
    """
    Responsável por testar a estrutura de dados.
    """
    @classmethod
    def setUpTestData(cls):
        settings.DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
            }
        }
        Autor.objects.create(nome="Ferdinando Americo")
        autor = Autor.objects.get(id=1)
        Noticia.objects.create(
            titulo="Noticia do dia",
            texto="Um texto de exemplo para está noticia.",
            autor=autor
        )

    def test_campo_nome(self):
        noticia = Noticia.objects.get(id=1)
        campo_titulo = noticia._meta.get_field('titulo').verbose_name
        campo_texto = noticia._meta.get_field('texto').verbose_name
        campo_autor = noticia._meta.get_field('autor').verbose_name
        self.assertEquals(campo_titulo, 'titulo')
        self.assertEquals(campo_texto, 'texto')
        self.assertEquals(campo_autor, 'autor')

    def test_campo_nome_max_length(self):
        noticia = Noticia.objects.get(id=1)
        max_length_titulo = noticia._meta.get_field('titulo').max_length
        self.assertEquals(max_length_titulo, 150)
