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
    def validar_cpf(self, valor):
        if len(valor) != 11:
            raise ValueError("CPF INVÁLIDO")
        self._cpf = valor 


    @property 
    def email(self):
        return self._email
    
    @email.setter
    def validar_email(self, valor):
        if "@" not in valor:
            raise ValueError("EMAIL INVALIDO")

    #CRUD completo 

    def cadastrar(self):
        pass

    def atualizar(self):
        pass 

    def deletar(self):
        pass

    def buscar(self):
        pass 
