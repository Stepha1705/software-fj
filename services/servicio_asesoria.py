from models.servicio import Servicio

class ServicioAsesoria(Servicio):

    def __init__(self, horas):
        super().__init__("Asesoría")
        self.horas = horas

    def calcular_costo(self):
        return self.horas * 100

    def descripcion(self):
        return f"Asesoría por {self.horas} horas"
    