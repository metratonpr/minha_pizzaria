"""
URL configuration for pizzaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importa o módulo de administração padrão do Django
from django.contrib import admin
# Importa a função 'path' para definir rotas e 'include' para incluir rotas de outros aplicativos
from django.urls import path, include
# Importa as configurações do projeto (definidas no arquivo settings.py)
from django.conf import settings
# Importa a função para servir arquivos estáticos (como imagens) durante o desenvolvimento
from django.conf.urls.static import static

# Lista principal de rotas do projeto
urlpatterns = [
    # Rota para acessar o painel de administração do Django
    path("admin/", admin.site.urls),
    # Inclui as rotas do aplicativo 'cardapio' na raiz do site ('')
    path('', include('cardapio.urls')),
]

# Se o modo DEBUG estiver ativo (ou seja, em ambiente de desenvolvimento)
if settings.DEBUG:
    # Configura o Django para servir arquivos de mídia (uploads, imagens, etc.)
    # diretamente pela aplicação (apenas em desenvolvimento, não em produção).
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)