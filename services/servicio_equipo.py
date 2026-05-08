from models.servicio import Servicio

class ServicioEquipo(Servicio):

    TARIFAS = {
        "Laptop": 40000,
        "VideoBeam": 60000,
        "Impresora": 30000
    }

    def __init__(self, equipo: str, horas: float):

        if equipo not in self.TARIFAS:
            raise ValueError("Equipo no disponible")

        super().__init__(horas)

        self.__equipo = equipo

    def calcular_costo(self):

        return self._unidades * self.TARIFAS[self.__equipo]

    def descripcion(self):

        return f"Alquiler de {self.__equipo} por {self._unidades:.1f} horas"