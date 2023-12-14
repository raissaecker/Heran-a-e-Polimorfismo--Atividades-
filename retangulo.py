from forma_geometrica import FormaGeometrica

class Retangulo(FormaGeometrica):
    """Calcula a área e o perímetro do retângulo"""

    def __init__(self, comprimento: float, largura: float):
        """Obtém o valor do comprimento e largura do círculo"""
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        """Calcula a área do retângulo"""
        return self.comprimento * self.largura
    
    def calcular_perimetro(self):
        """Calcula o perímetro do retângulo"""
        return 2 * (self.comprimento + self.largura)