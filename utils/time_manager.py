from datetime import datetime


class TimeManager:
    @staticmethod
    def calcular_horas(hora_inicio: str, hora_fin: str) -> float:
        formato = "%H:%M"

        inicio = datetime.strptime(hora_inicio, formato)
        fin = datetime.strptime(hora_fin, formato)

        horas = (fin - inicio).seconds / 3600

        if horas <= 0:
            raise ValueError("Horario inválido")

        return horas
    