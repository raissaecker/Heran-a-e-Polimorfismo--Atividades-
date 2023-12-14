from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    """A classe representa uma forma geométrica"""

    @abstractmethod
    def calcular_area(self) -> float:
        pass
    
    @abstractmethod
    def calcular_perimetro(self) -> float:
        pass
        
