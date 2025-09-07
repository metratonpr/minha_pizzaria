"""
ASGI config for pizzaria project.

Esse arquivo configura a interface ASGI do Django.
O ASGI é um padrão moderno de comunicação entre servidores e frameworks Python,
substituto/alternativa do WSGI (mais antigo).

Ele permite que sua aplicação Django rode de forma assíncrona,
suportando WebSockets, HTTP/2, e long-polling.

O Django usa esse arquivo automaticamente quando você executa o projeto
em servidores compatíveis (como Daphne ou Uvicorn).
"""

import os  # Biblioteca padrão para manipulação de variáveis de ambiente

# Importa a função que cria a aplicação ASGI do Django
from django.core.asgi import get_asgi_application

# Define a variável de ambiente que indica onde estão as configurações do projeto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzaria.settings")

# Cria a aplicação ASGI que será usada pelo servidor
application = get_asgi_application()
