class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  
        self.idade = idade  

    def mostrar_info(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}')

pessoa1 = Pessoa('José', 30)
pessoa1.mostrar_info()    

pessoa2 = Pessoa('Maria', 30)
pessoa2.mostrar_info() 

pessoa3 = Pessoa('Cleber', 30)
pessoa3.mostrar_info() 

