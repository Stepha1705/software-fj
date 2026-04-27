from abc import ABC, abstractmethod
from exceptions.errores import ServicioInvalidoError


class Servicio(ABC):
    def __init__(self, unidades: float):
        if unidades <= 0:
            raise ServicioInvalidoError("Las unidades deben ser mayores a cero")
        self._unidades = unidades

    @abstractmethod
    def calcular_costo(self) -> float:
        pass

    @abstractmethod
    def descripcion(self) -> str:
        pass
    