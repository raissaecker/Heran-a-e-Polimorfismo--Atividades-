from animal import Animal

class Passaro(Animal):
        def emitir_som(self):
            print(f"{self.nome} faz piu piu!")
        
        def mover(self):
            print(f"{self.nome} voa!")