from animal import Animal

class Cachorro(Animal):
        def emitir_som(self):
            print(f"{self.nome} latiu!")
        
        def mover(self):
            print(f"{self.nome} corre!")