from forma_geometrica import FormaGeometrica
import math

class Circulo(FormaGeometrica):
    """Calcula a área e o perímetro do círculo"""

    def __init__(self, raio: float):
        """Obtém o valor do raio do círculo"""
        self.raio = raio

    def calcular_area(self):
        """Calcula a área do círculo"""
        return math.pi * self.raio ** 2
    
    def calcular_perimetro(self):
        """Calcula o perímetro do círculo"""
        return 2 * math.pi * self.raio