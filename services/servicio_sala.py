from models.servicio import Servicio


class ServicioSala(Servicio):
    TARIFAS = {
        "Sala A": 50000,
        "Sala B": 75000,
        "Sala Premium": 120000
    }

    def __init__(self, sala: str, horas: float):
        if sala not in self.TARIFAS:
            raise ValueError("Sala no disponible")

        super().__init__(horas)
        self._sala = sala

    def calcular_costo(self) -> float:
        return self._unidades * self.TARIFAS[self._sala]

    def descripcion(self) -> str:
        return f"Reserva de {self._sala} por {self._unidades:.1f} horas"