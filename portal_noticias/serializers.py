from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Autor, Noticia


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome']


class NoticiaSerializer(ModelSerializer):
    nome_autor = ReadOnlyField()

    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'texto', 'autor', 'nome_autor']
