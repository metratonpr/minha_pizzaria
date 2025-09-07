from django.shortcuts import render, get_object_or_404
from .models import Pizza, TipoPizza, Ingrediente, IngredientePizza, TipoIngrediente

# Create your views here.
def home(request):
    """Página inicial - nosso cardápio"""
    pizzas_salgadas = Pizza.objects.filter(tipo_pizza__nome='Salgada', ativa=True)
    pizzas_doces = Pizza.objects.filter(tipo_pizza__nome='Doce', ativa=True)
    
    context = {
        'pizzas_salgadas': pizzas_salgadas,
        'pizzas_doces': pizzas_doces,
    }
    return render(request, 'cardapio/home.html', context)

def detalhe_pizza(request, pizza_id):
    """Página de detalhes de uma pizza"""
    pizza = get_object_or_404(Pizza, id=pizza_id)
    ingredientes = IngredientePizza.objects.filter(pizza=pizza)
    
    # Calcular custo total dos ingredientes
    custo_total_ingredientes = sum(ing.custo_ingrediente for ing in ingredientes)
    
    context = {
        'pizza': pizza,
        'ingredientes': ingredientes,
        'custo_total_ingredientes': custo_total_ingredientes,
    }
    return render(request, 'cardapio/detalhe_pizza.html', context)

def ingredientes(request):
    """Página com todos os ingredientes"""
    tipos_ingredientes = TipoIngrediente.objects.all()
    
    context = {
        'tipos_ingredientes': tipos_ingredientes,
    }
    return render(request, 'cardapio/ingredientes.html', context)