class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print('au au!')

class Gato(Animal):
    def fazer_som(self):
        print('Meauu!')

cachorro = Cachorro('Rex')
gato= Gato('Elvis')

cachorro.fazer_som()
gato.fazer_som()