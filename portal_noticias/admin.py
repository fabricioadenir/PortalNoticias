from django.contrib import admin
from .models import Autor, Noticia


class AutorAdmin(admin.ModelAdmin):
    model = Autor
    campos_autor = ['id', 'nome']
    list_display = campos_autor
    list_filter = campos_autor
    search_fields = campos_autor


admin.site.register(Autor, AutorAdmin)


class NoticiaAdmin(admin.ModelAdmin):
    model = Noticia

    list_display = ['id', 'titulo', 'texto', 'autor']
    list_filter = ['id', 'titulo', 'autor']
    search_fields = ['id', 'titulo', 'texto', 'autor__nome']


admin.site.register(Noticia, NoticiaAdmin)
