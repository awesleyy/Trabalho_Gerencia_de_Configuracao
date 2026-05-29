class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        self.itens.append({"produto": produto, "quantidade": quantidade})

    def remover_item(self, produto):
        self.itens = [item for item in self.itens if item["produto"] != produto]

    def calcular_total(self):
        return sum(item["produto"].preco * item["quantidade"] for item in self.itens)

    def limpar(self):
        self.itens = []