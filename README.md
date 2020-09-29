<img src="docs/news.png" width="123px" alt="verifica.me" align="right">

# Portal de Notícias
# v0.1.0

Esta API responsável por implementar um portal de notícias, tendo como objetivo realizar cadastro de autores e suas publicações.

**Instalação e configuração** https://github.com/fabricioadenir/PortalNoticias/blob/master/ROI.md

***
Depende de:
* [Python 3](https://www.python.org/downloads/) (3+)
* [MongoDB](https://www.mongodb.com/dr/fastdl.mongodb.org/windows/mongodb-windows-x86_64-4.4.1-signed.msi/download)

# Subindo API com docker:
Docker é responsável pela construção da API e MongoDB.

* Comando para criação e execução.
```
docker-compose up -d --build
```
## Painel Django Rest para utilizar de forma direta na API.

* Exemplo: http://IP:PORT por default é: http://localhost:8000

## Painel Admin do Django

* Seguindo o exempo: http://localhost:8000/admin

## Documentação da API em tempo de execução

* Seguindo o exemplo: http://localhost:8000/redoc

&nbsp;

# EndPoit e como usar:
Para facilitar o uso e exemplicar como a API trabalha [clique aqui](https://fabricioadenir.github.io/PortalNoticias/) e veja a documentação de uso.

&nbsp;

# Executar testes
```sh
$ python manage.py test portal_noticias/tests --verbosity 2
```

&nbsp;

# Lint
```sh
$ flake8 --config=flake8
```
```sh
$ pycodestyle --config=pycodestyle .
```

## Contato


[Fabricio Silva](mailto:fabricioadenir@gmail.com)