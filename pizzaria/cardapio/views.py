# Importa a função 'render' para renderizar templates HTML
# Importa 'get_object_or_404' para buscar objetos no banco e retornar erro 404 caso não exista
from django.shortcuts import render, get_object_or_404

# Importa os modelos que representam tabelas no banco de dados
from .models import Pizza, TipoPizza, Ingrediente, IngredientePizza, TipoIngrediente

# -------------------------------
# VIEW 1: Página inicial do cardápio
# -------------------------------
def home(request):
    """Página inicial - nosso cardápio"""

    # Busca todas as pizzas do tipo "Salgada" que estão ativas no cardápio
    pizzas_salgadas = Pizza.objects.filter(tipo_pizza__nome='Salgada', ativa=True)

    # Busca todas as pizzas do tipo "Doce" que estão ativas
    pizzas_doces = Pizza.objects.filter(tipo_pizza__nome='Doce', ativa=True)
    
    # Dicionário com os dados que serão enviados ao template
    context = {
        'pizzas_salgadas': pizzas_salgadas,
        'pizzas_doces': pizzas_doces,
    }
    # Renderiza o template 'home.html', passando o contexto acima
    return render(request, 'cardapio/home.html', context)

# -------------------------------
# VIEW 2: Detalhes de uma pizza específica
# -------------------------------
def detalhe_pizza(request, pizza_id):
    """Página de detalhes de uma pizza"""

    # Busca a pizza pelo ID recebido na URL
    # Se não existir, retorna página de erro 404
    pizza = get_object_or_404(Pizza, id=pizza_id)

    # Busca todos os ingredientes relacionados a essa pizza
    ingredientes = IngredientePizza.objects.filter(pizza=pizza)
    
    # Calcular custo total dos ingredientes
    custo_total_ingredientes = sum(ing.custo_ingrediente for ing in ingredientes)
    
    # Monta o contexto com pizza, ingredientes e o custo total
    context = {
        'pizza': pizza,
        'ingredientes': ingredientes,
        'custo_total_ingredientes': custo_total_ingredientes,
    }

     # Renderiza o template 'detalhe_pizza.html', passando o contexto
    return render(request, 'cardapio/detalhe_pizza.html', context)

# -------------------------------
# VIEW 3: Lista de todos os ingredientes disponíveis
# -------------------------------
def ingredientes(request):
    """Página com todos os ingredientes"""

    # Busca todos os tipos de ingredientes (ex: queijos, molhos, carnes, etc.)
    tipos_ingredientes = TipoIngrediente.objects.all()
    
    # Monta o contexto com os tipos de ingredientes
    context = {
        'tipos_ingredientes': tipos_ingredientes,
    }

    # Renderiza o template 'ingredientes.html', passando os dados
    return render(request, 'cardapio/ingredientes.html', context)