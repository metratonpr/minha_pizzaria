from django.urls import path
from . import views

app_name = 'cardapio'

urlpatterns = [
    path('', views.home, name='home'),
    path('pizza/<int:pizza_id>/', views.detalhe_pizza, name='detalhe_pizza'),
    path('ingredientes/', views.ingredientes, name='ingredientes'),
]