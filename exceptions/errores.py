class ErrorSistema(Exception):
    """Excepción base del sistema"""
    pass


class ClienteInvalidoError(ErrorSistema):
    pass


class ServicioInvalidoError(ErrorSistema):
    pass


class AutenticacionError(ErrorSistema):
    pass

def registrar_error(mensaje):
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(mensaje + "\n")

