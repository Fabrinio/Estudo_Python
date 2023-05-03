class Produto:
    def __init__(self, codigo, descricao, preco_custo):
        self.codigo = codigo
        self.descricao = descricao
        self.preco_custo = preco_custo
        self.margem_lucro = None
        self.preco_venda = None

    def setMargemLucro(self, percentual):
        self.margem_lucro = percentual
        self.preco_venda = self.preco_custo * (1 + self.margem_lucro/100)

    def setPrecoVenda(self, valor):
        self.preco_venda = valor
        self.margem_lucro = (self.preco_venda - self.preco_custo) / self.preco_custo * 100

    def __str__(self):
        return f"Código: {self.codigo}\nDescrição: {self.descricao}\nPreço de custo: R$ {self.preco_custo:.2f}\nMargem de lucro: {self.margem_lucro:.2f}%\nPreço de venda: R$ {self.preco_venda:.2f}"

# criando um produto com código 1, descrição "Caneta" e preço de custo R$ 1,00
p = Produto(1, "Caneta", 1.0)

# definindo a margem de lucro como 50%
p.setMargemLucro(50)

# imprimindo as informações do produto
print(p)

# alterando o preço de venda para R$ 3,00
p.setPrecoVenda(3.0)

# imprimindo as informações do produto novamente
print(p)
