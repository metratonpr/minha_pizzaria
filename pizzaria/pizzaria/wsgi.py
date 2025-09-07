"""
WSGI config for pizzaria project.

Esse arquivo configura a interface WSGI do Django.
O WSGI é um padrão de comunicação entre servidores web (ex: Apache, Nginx, Gunicorn)
e frameworks Python como o Django.

➡ Em resumo: ele permite que o servidor "converse" com o Django.

Quando você roda em produção com servidores tradicionais,
esse arquivo é o ponto de entrada.
"""

import os  # Biblioteca padrão para lidar com variáveis de ambiente e sistema

# Importa a função que cria a aplicação WSGI do Django
from django.core.wsgi import get_wsgi_application

# Define a variável de ambiente que aponta para o arquivo de configurações do projeto
# (nesse caso: pizzaria/settings.py)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzaria.settings")

# Cria a aplicação WSGI que será usada pelo servidor
application = get_wsgi_application()
