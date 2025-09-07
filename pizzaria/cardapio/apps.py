# Importa a classe base para configurar aplicativos no Django
from django.apps import AppConfig


# Classe de configuração do app 'cardapio'
class CardapioConfig(AppConfig):
    # Define o tipo padrão de chave primária para os modelos
    # "BigAutoField" cria IDs automáticos grandes (inteiros de 64 bits)
    default_auto_field = "django.db.models.BigAutoField"

    # Nome do app, deve ser igual ao nome da pasta do app
    name = "cardapio"
