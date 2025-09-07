from django.contrib import admin
from django.utils.html import format_html
from .models import TipoPizza, TipoIngrediente, Ingrediente, Pizza, IngredientePizza

# Registrando TipoPizza
@admin.register(TipoPizza)
class TipoPizzaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']

# Registrando TipoIngrediente  
@admin.register(TipoIngrediente)
class TipoIngredienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'icone']

# Registrando Ingrediente
@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo_ingrediente', 'preco_formatado', 'disponivel']
    list_filter = ['tipo_ingrediente', 'disponivel']
    
    def preco_formatado(self, obj):
        return f'R$ {obj.preco_por_unidade:.2f}/{obj.unidade_medida}'
    preco_formatado.short_description = 'Preço'

# Configuração para adicionar ingredientes na página da pizza
class IngredientePizzaInline(admin.TabularInline):
    model = IngredientePizza
    extra = 1
    fields = ['ingrediente', 'quantidade_numerica', 'quantidade_texto']

# Registrando Pizza
@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo_pizza', 'preco_total_formatado', 'tempo_preparo', 'ativa']
    list_filter = ['tipo_pizza', 'ativa']
    inlines = [IngredientePizzaInline]
    
    def preco_total_formatado(self, obj):
        return f'R$ {obj.preco_total:.2f}'
    preco_total_formatado.short_description = 'Preço Total'

# Personalizando o título do admin
admin.site.site_header = "SENAC PIZZA - Administração"
admin.site.site_title = "Pizzaria Admin"