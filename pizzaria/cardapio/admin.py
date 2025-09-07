# Importa os recursos do Django Admin
from django.contrib import admin

# Importa utilitário para formatar HTML dentro do Admin (não está sendo usado ainda, mas pode servir para ícones, cores etc.)
from django.utils.html import format_html

# Importa os modelos criados no app 'cardapio'
from .models import TipoPizza, TipoIngrediente, Ingrediente, Pizza, IngredientePizza


# -----------------------------
# REGISTRO DO MODELO TipoPizza
# -----------------------------
@admin.register(TipoPizza)  # Registra o modelo no painel admin
class TipoPizzaAdmin(admin.ModelAdmin):  
    # Define quais campos vão aparecer na listagem de Tipos de Pizza
    list_display = ['nome', 'descricao']


# -----------------------------
# REGISTRO DO MODELO TipoIngrediente
# -----------------------------
@admin.register(TipoIngrediente)
class TipoIngredienteAdmin(admin.ModelAdmin):
    # Mostra o nome e o emoji/ícone na listagem do Admin
    list_display = ['nome', 'icone']


# -----------------------------
# REGISTRO DO MODELO Ingrediente
# -----------------------------
@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    # Campos que aparecem na listagem de Ingredientes
    list_display = ['nome', 'tipo_ingrediente', 'preco_formatado', 'disponivel']

    # Filtros laterais para facilitar busca
    list_filter = ['tipo_ingrediente', 'disponivel']
    
    # Função personalizada para formatar o preço (ex: R$ 5.00/kg)
    def preco_formatado(self, obj):
        return f'R$ {obj.preco_por_unidade:.2f}/{obj.unidade_medida}'

    # Nome da coluna no Admin
    preco_formatado.short_description = 'Preço'


# -----------------------------
# INLINE: Ingredientes dentro da Pizza
# -----------------------------
class IngredientePizzaInline(admin.TabularInline):
    # Define o modelo de ligação entre Pizza e Ingrediente
    model = IngredientePizza

    # Quantos campos extras (em branco) aparecem por padrão
    extra = 1

    # Quais campos mostrar no inline (ingrediente + quantidades)
    fields = ['ingrediente', 'quantidade_numerica', 'quantidade_texto']


# -----------------------------
# REGISTRO DO MODELO Pizza
# -----------------------------
@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    # Quais colunas aparecem na listagem de Pizzas
    list_display = ['nome', 'tipo_pizza', 'preco_total_formatado', 'tempo_preparo', 'ativa']

    # Adiciona filtros no painel lateral
    list_filter = ['tipo_pizza', 'ativa']

    # Permite editar ingredientes diretamente dentro da página da Pizza
    inlines = [IngredientePizzaInline]
    
    # Função para formatar o preço total da pizza
    def preco_total_formatado(self, obj):
        return f'R$ {obj.preco_total:.2f}'
    
    # Nome da coluna no Admin
    preco_total_formatado.short_description = 'Preço Total'


# -----------------------------
# PERSONALIZAÇÃO DO ADMIN GERAL
# -----------------------------
# Título no cabeçalho do painel administrativo
admin.site.site_header = "SENAC PIZZA - Administração"

# Nome que aparece na aba do navegador
admin.site.site_title = "Pizzaria Admin"
