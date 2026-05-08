from models.servicio import Servicio

class ServicioAsesoria(Servicio):

    TARIFAS = {
        "Programación": 90000,
        "Bases de Datos": 110000,
        "Redes": 80000
    }

    def __init__(self, tipo: str, horas: float):

        if tipo not in self.TARIFAS:
            raise ValueError("Asesoría no disponible")

        super().__init__(horas)

        self.__tipo = tipo

    def calcular_costo(self):

        return self._unidades * self.TARIFAS[self.__tipo]

    def descripcion(self):

        return f"Asesoría en {self.__tipo} por {self._unidades:.1f} horas"