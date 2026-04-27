from models.servicio import Servicio

class ServicioEquipo(Servicio):

    def __init__(self, dias):
        super().__init__("Equipo")
        self.dias = dias

    def calcular_costo(self):
        return self.dias * 30

    def descripcion(self):
        return f"Alquiler de equipo por {self.dias} días"
    