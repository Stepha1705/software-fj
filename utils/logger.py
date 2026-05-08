from datetime import datetime

class Logger:

    @staticmethod
    def registrar_error(error):
        with open("logs.txt", "a", encoding="utf-8") as archivo:
            archivo.write(
                f"[ERROR] {datetime.now()} - {error}\n"
            )

    @staticmethod
    def registrar_evento(evento):
        with open("logs.txt", "a", encoding="utf-8") as archivo:
            archivo.write(
                f"[EVENTO] {datetime.now()} - {evento}\n"
            )