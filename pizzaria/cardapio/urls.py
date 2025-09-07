# Importa a função 'path' usada para mapear URLs para funções (views)
from django.urls import path

# Importa o módulo de views (as funções que tratam as requisições HTTP)
from . import views

# Define um namespace para as rotas deste app
# Isso permite diferenciar URLs de outros apps quando usado em templates ou redirecionamentos
app_name = 'cardapio'

# Lista de rotas específicas para o app 'cardapio'
urlpatterns = [
    # Rota para a página inicial (raiz do app), chama a função 'home' da views
    # Nome 'home' permite referenciar essa rota em templates ou redirecionamentos
    path('', views.home, name='home'),
    # Rota dinâmica para exibir os detalhes de uma pizza específica
    # <int:pizza_id> captura um número da URL e passa como parâmetro para a função 'detalhe_pizza'
    path('pizza/<int:pizza_id>/', views.detalhe_pizza, name='detalhe_pizza'),

    # Rota para listar ingredientes disponíveis, chama a função 'ingredientes'
    path('ingredientes/', views.ingredientes, name='ingredientes'),
]