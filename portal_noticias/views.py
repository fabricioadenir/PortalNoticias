from rest_framework.viewsets import ModelViewSet
from .models import Autor, Noticia
from .serializers import AutorSerializer, NoticiaSerializer

from rest_framework import filters
from rest_framework.generics import ListCreateAPIView


# Responsável pelos métodos de ['PUT', 'PATCH', 'DELETE']
class AutorViewSet(ModelViewSet):
    """
    Além de permitir pesquisar por autor pelo 'id'. Também é possível realizar
    a pesquisa
    no seguinte formato:\n
    api/autores?search={valor}

    {valor} =  Pode ser qualquer valor string ou integer, pode conter mais de um valor. Exemplo:\n
    api/autores?search=novidade fernando \n

    A API irá fazer um filtro retornando
    os autores que existirem com o valor pesquisado, filtrando em (titulo, texto e autor).
    """
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


# Responsável pelos métodos de ['GET', 'POST']
class AutorViewList(ListCreateAPIView):
    search_fields = ['id', 'nome']
    filter_backends = (filters.SearchFilter,)
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


# Responsável pelos métodos de ['PUT', 'PATCH', 'DELETE']
class NoticiaViewSet(ModelViewSet):
    """
    Além de permitir pesquisar por noticias pelo 'id'. Também é possível realizar
    a pesquisa
    no seguinte formato:\n
    api/noticias?search={valor}

    {valor} =  Pode ser qualquer valor string ou integer, pode conter mais de um valor. Exemplo:\n
    api/noticias?search=novidade fernando \n

    A API irá fazer um filtro retornando
    as noticias que existirem com o valor pesquisado, filtrando em (titulo, texto e autor).
    """
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer


# Responsável pelos métodos de ['GET', 'POST']
class NoticiaViewList(ListCreateAPIView):
    search_fields = ['titulo', 'texto', 'autor__nome']
    filter_backends = (filters.SearchFilter,)
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
