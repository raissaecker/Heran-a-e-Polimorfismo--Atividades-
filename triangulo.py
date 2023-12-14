from forma_geometrica import FormaGeometrica

class Triangulo(FormaGeometrica):
    """Calcula a área e o perímetro do triângulo"""

    def __init__(self, base: float, altura: float, ladoA: float, ladoB: float, ladoC: float):
        """Obtém o valor da base, altura e lados do triângulo"""
        self.base = base
        self.altura = altura
        self.ladoA = ladoA
        self.ladoB = ladoB 
        self.ladoC = ladoC


    def calcular_area(self):
        """Calcula a área do triângulo"""
        return 0.5 * self.base * self.altura

    def calcular_perimetro(self):
        """Calcula o perímetro do triângulo"""
        return self.lado1 + self.lado2 + self.lado3