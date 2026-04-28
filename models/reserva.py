class Reserva:
    def __init__(self, cliente, servicio):
        self._cliente = cliente
        self._servicio = servicio
        self._estado = "Confirmada"

    def cancelar(self):
        self._estado = "Cancelada"

    def resumen(self):
        return {
            "cliente": str(self._cliente),
            "servicio": self._servicio.descripcion(),
            "costo": self._servicio.calcular_costo(),
            "estado": self._estado
        }
    