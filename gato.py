from animal import Animal

class Gato(Animal):
        def emitir_som(self):
            print(f"{self.nome} miou!")
        
        def mover(self):
            print(f"{self.nome} pula!")