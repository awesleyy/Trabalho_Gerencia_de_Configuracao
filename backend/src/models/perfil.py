class perfil():
    def __init__(self, nome, idade, email, senha):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.senha = senha

    def editar_usuario(self):
        nome = str(input("Digite o seu nome: "))
        self.nome = nome
        idade = str(input("Digite a sua idade: "))
        self.idade = idade
        email = str(input("Digite o seu email: "))
        self.email = email
        senha = str(input("Digite a sua senha: "))
        self.senha = senha

