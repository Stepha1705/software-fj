class ErrorSistema(Exception):
    """Excepción base del sistema"""
    pass


class ClienteInvalidoError(ErrorSistema):
    pass


class ServicioInvalidoError(ErrorSistema):
    pass


class AutenticacionError(ErrorSistema):
    pass
