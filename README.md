# agenda_python

Agenda criada durante o curso da Digital Inovation One

Python + Django + Pycharm

#Comandos DJango:

Criar um projeto com pasta inical do Django (com arquivos inicias manager e etc):

	django-admin startproject myproject
	
Criar pasta core (com arquivos inicias de views e etc) em um projeto Django:

	django-admin startapp core


Criar tabela inicial (admin) no Django:

	python manage.py migrate (migra qualquer classe existente como uma tabela no BD)
	
	python manage.py createsuperuser --username admin (adicionar emais, senha, etc em seguida)
	
	Acessar: http://127.0.0.1:8000/admin/
	
Criar nova tabela:
	
	python manage.py makemigrations core
	python manage.py sqlmigrate core 0001 (Ex: 0001 = nome do arquivo criado na tabela migration/)
	python manage.py migrate core 0001

#Configurar Django no Pycharm:

Adicionar virtualenv criada:

    Settings -> Project interpreter -> Show All -> Botão + -> Escolha a virtualenv que foi criada anteriormente 

Caminho relativo:
 
    C:/minhas_virtualenv/meu_projeto/Scripts/python.exe

 - Abrir arquivo manage.py e rodar... vai dar erro
 - Edirar o runner criado na barra superior (com o nome 'manage')
 - Adicionar o paramêtro 'runserver' no campo parameters -> Apply
 - Rode novamente o arquivo manage.py
 - Isso vai executar o server do Django no endereço http://127.0.0.1:8000/

#Sobre virtualenv:

Instalar virtualenv:

	pip install virtualenv
	
Criar nova virtualenv:

 - Escolha a pasta default Ex.: C:/minhas_virtualenvs
 
        virtualenv nome_da_virtualenv

Ativar/desativar Virtualenv:

    nome_da_virtualenv/Scripts/activate
    deactivate

Outros:
 
    pip freeze (listar)