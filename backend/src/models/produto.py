class Produto():
    def __init__(self, nome, categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
    
    @staticmethod
    def cadastrar_produto():
        nome = str(input("Digite o nome do produto: "))
        categoria = str(input("Digite a categoria do produto: "))
        preco = float(input("Digite o preço do produto: "))

        novo_produto = Produto(nome, categoria, preco)
        return novo_produto
    
    def editar_preco(self):
        novo_preco = float(input("Digite o novo valor do produto: "))
        self.preco = novo_preco