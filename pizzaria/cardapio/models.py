from django.db import models  # Importa os tipos de campos e relacionamentos do Django ORM


# -------------------------------
# MODELO: Tipo de Pizza
# Exemplo: Doce, Salgada, Mista
# -------------------------------
class TipoPizza(models.Model):
    # Nome do tipo de pizza (ex: "Salgada")
    nome = models.CharField(max_length=50)  # Texto curto

    # Descrição opcional (ex: "Tradicional, com sabores variados")
    descricao = models.TextField(blank=True)  # Texto longo, pode ficar em branco

    # Cor para personalização (ex: para destacar no cardápio online)
    cor_hex = models.CharField(max_length=7, default="#FF6B6B")  # Cor no formato HEX (#RRGGBB)

    def __str__(self):
        # Exibe o nome quando o objeto for mostrado no Django Admin
        return self.nome


# -------------------------------
# MODELO: Tipo de Ingrediente
# Exemplo: Queijos, Molhos, Carnes
# -------------------------------
class TipoIngrediente(models.Model):
    nome = models.CharField(max_length=100)  # Nome da categoria do ingrediente
    icone = models.CharField(max_length=50)  # Emoji ou ícone para representar a categoria
    
    def __str__(self):
        return self.nome


# -------------------------------
# MODELO: Ingrediente
# Cada ingrediente tem preço e unidade de medida
# -------------------------------
class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)  # Nome do ingrediente (ex: "Mussarela")

    # Relacionamento: cada ingrediente pertence a um TipoIngrediente
    tipo_ingrediente = models.ForeignKey(TipoIngrediente, on_delete=models.CASCADE)

    # Preço unitário (ex: 0.05 R$/g)
    preco_por_unidade = models.DecimalField(max_digits=8, decimal_places=3, default=0.00)

    # Unidade de medida (ex: g, ml, unidade)
    unidade_medida = models.CharField(max_length=20, default="g")

    # Disponibilidade no estoque
    disponivel = models.BooleanField(default=True)
    
    def __str__(self):
        # Exibe nome + preço no admin
        return f"{self.nome} - R${self.preco_por_unidade}/{self.unidade_medida}"


# -------------------------------
# MODELO: Pizza
# Representa uma pizza completa no cardápio
# -------------------------------
class Pizza(models.Model):
    nome = models.CharField(max_length=100)         # Nome da pizza (ex: "Calabresa")
    descricao = models.TextField()                  # Descrição do sabor
    tipo_pizza = models.ForeignKey(TipoPizza, on_delete=models.CASCADE)  # Relacionamento com TipoPizza

    # Foto opcional da pizza
    foto = models.ImageField(upload_to='pizzas/', blank=True, null=True)

    # Preço base (massa, molho, preparo)
    preco_base = models.DecimalField(max_digits=8, decimal_places=2)

    # Texto explicando o modo de preparo
    modo_preparo = models.TextField()

    # Tempo estimado de preparo (em minutos)
    tempo_preparo = models.IntegerField()

    # Define se a pizza está ativa no cardápio
    ativa = models.BooleanField(default=True)

    # Data de criação (gerada automaticamente)
    criada_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    
    @property
    def preco_total(self):
        """Calcula o preço total = preço base + custo dos ingredientes"""
        total = self.preco_base
        # Percorre todos os ingredientes ligados a essa pizza
        for ingrediente_pizza in self.ingredientepizza_set.all():
            total += ingrediente_pizza.custo_ingrediente
        return total


# -------------------------------
# MODELO: IngredientePizza
# Tabela intermediária que liga Pizza ↔ Ingrediente
# -------------------------------
class IngredientePizza(models.Model):
    # Relaciona cada ingrediente a uma pizza
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)

    # Quantidade usada (número)
    quantidade_numerica = models.DecimalField(max_digits=8, decimal_places=2)

    # Quantidade textual (ex: "1 fatia", "meia colher"), opcional
    quantidade_texto = models.CharField(max_length=50, blank=True)
    
    @property
    def custo_ingrediente(self):
        """Multiplica quantidade × preço unitário para calcular o custo"""
        return self.quantidade_numerica * self.ingrediente.preco_por_unidade
    
    @property
    def quantidade_display(self):
        """Exibe a quantidade de forma amigável"""
        if self.quantidade_texto:
            return f"{self.quantidade_numerica}{self.ingrediente.unidade_medida} ({self.quantidade_texto})"
        return f"{self.quantidade_numerica}{self.ingrediente.unidade_medida}"
