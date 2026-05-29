class Cliente:
    def __init__(self, nome, cpf, email, endereco):
        self.nome = nome 
        self._cpf = cpf 
        self._email = email 
        self.endereco = endereco 
        
    #Validações

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        if len(valor) != 11 or not valor.isdigit():
            raise ValueError("CPF inválido")
        self._cpf = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if "@" not in valor or "." not in valor:
            raise ValueError("Email inválido")
        self._email = valor

    #CRUD completo 

    def cadastrar(self):
        pass

    def atualizar(self):
        pass 

    def deletar(self):
        pass

    def buscar(self):
        pass 


cliente1 = Cliente("Henrique Coimbra", "10318182432", "coimbr23a@gmail.com", "Rua jose arnaldo jatay pedrosa")

cliente1.cadastrar()