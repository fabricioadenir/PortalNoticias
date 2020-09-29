<img src="docs/roi.png" width="123px" alt="verifica.me" align="right">

# Portal de Notícias
# v0.1.0

## Configuração e inicialização usando Docker.
Esse ambiente foi preparado para ser instalado no Docker seguindo os passos abaixo e o banco de dados MongoDB:

* Comando responsável pela criação da imagem e subir a API e o MongoDB.
```
docker-compose up -d --build
```

## Instalação e configuração ambiente local (Dev).
***
Depende de:
* [Python 3](https://www.python.org/downloads/) (3+)
* [MongoDB](https://www.mongodb.com/dr/fastdl.mongodb.org/windows/mongodb-windows-x86_64-4.4.1-signed.msi/download)

Se for utilizado o Docker para criar a imagem do MongoDB.

* O banco de dados MongoDB pode ser construido através do docker-compose com o seguinte comando.
```
docker-compose up -d --build --no-deps mongo
```

Caso não opte em utilizar o Docker:
1. Baixar o [MongoDB](https://www.mongodb.com/dr/fastdl.mongodb.org/windows/mongodb-windows-x86_64-4.4.1-signed.msi/download)
2. Criar usuário Admin:
```sh
$ mongo admin
> use admin
switched to db admin
> db.createUser({ user: "admin", pwd: "admin", roles: [{role: "userAdminAnyDatabase", db: "admin"}]});
> exit
```
2. Criar o usuário que API irá usar para acessar o banco de dados, os novos usuários precisam ser criados na collection **admin**. O acesso  desses usuários serão autênticados automaticamente nessa collection:

***Usuário default*** 'noticias'
***Senha default*** 'noticias123'

```sh
$ mongo -u admin -p --authenticationDatabase admin
> use admin
switched to db admin
> db.createUser({ user: "noticias", pwd: "noticias123", roles: [{role: "readWrite", db: "portal"}]});
> exit
```

3. Instalar as dependências.
```sh
$ pip install -r requirements.txt
```

4. Montar a migração para o banco de dados.
```sh
$ python manage.py makemigrations
```

5. Realizar a migração da estrutura de dados para o banco.
```sh
$ python manage.py migrate
```

6. Criar alguns dados fictícios para testar a API.
```sh
$ python manage.py loaddata initial.json
```

7. Criação de usuário para que seja possível acessar o admin do Django.
```sh
$ python manage.py createsuperuser --email admin@example.com --username admin
```
***Obs***: O usuário criado será admin podendo escolher outro a seu critério.

8. Subir a API.
```sh
$ python manage.py runserver
```

&nbsp;

# EndPoit e como usar:
Para facilitar o uso e exemplicar como a API trabalha [clique aqui](https://fabricioadenir.github.io/PortalNoticias/) e veja a documentação de uso.

## Contato


[Fabricio Silva](mailto:fabricioadenir@gmail.com)