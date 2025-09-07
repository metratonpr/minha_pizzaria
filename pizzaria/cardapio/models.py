from django.db import models

# Create your models here.
#Tipos de Pizza (Doce, Salgada, Mista)
class TipoPizza(models.Model):
    nome = models.CharField(max_length=50) #Charfiel = Texto Curto
    descricao = models.TextField(blank=True) #TexField = Texto Longo
    cor_hex = models.CharField(max_length=7, default="#FF6B6B")

    def __str__(self):
        return self.nome

#Tipo de Ingredientes
class TipoIngrediente(models.Model):
    nome = models.CharField(max_length=100)
    icone = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

#Ingredientes com Preço
class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    tipo_ingrediente = models.ForeignKey(TipoIngrediente, on_delete=models.CASCADE)
    preco_por_unidade = models.DecimalField(max_digits=8, decimal_places=3, default=0.00)
    unidade_medida = models.CharField(max_length=20, default="g")
    disponivel = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nome} - R${self.preco_por_unidade}/{self.unidade_medida}"

#Enfim a Pizza
class Pizza(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    tipo_pizza = models.ForeignKey(TipoPizza, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='pizzas/', blank=True, null=True)
    preco_base = models.DecimalField(max_digits=8, decimal_places=2)
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    ativa = models.BooleanField(default=True)
    criada_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    
    @property
    def preco_total(self):
        """Aqui fazemos a conta: preço base + ingredientes"""
        total = self.preco_base
        for ingrediente_pizza in self.ingredientepizza_set.all():
            total += ingrediente_pizza.custo_ingrediente
        return total

#Ingredientes da Pizza
class IngredientePizza(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantidade_numerica = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade_texto = models.CharField(max_length=50, blank=True)
    
    @property
    def custo_ingrediente(self):
        """Multiplica quantidade × preço = custo do ingrediente"""
        return self.quantidade_numerica * self.ingrediente.preco_por_unidade
    
    @property
    def quantidade_display(self):
        """Mostra a quantidade de forma bonita"""
        if self.quantidade_texto:
            return f"{self.quantidade_numerica}{self.ingrediente.unidade_medida} ({self.quantidade_texto})"
        return f"{self.quantidade_numerica}{self.ingrediente.unidade_medida}"