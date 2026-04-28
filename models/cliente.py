from exceptions.errores import ClienteInvalidoError


class Cliente:
    def __init__(self, nombre: str, correo: str):
        if not nombre or not nombre.strip():
            raise ClienteInvalidoError("El nombre es obligatorio")

        if "@" not in correo:
            raise ClienteInvalidoError("Correo inválido")

        self._nombre = nombre
        self._correo = correo

    @property
    def nombre(self):
        return self._nombre

    @property
    def correo(self):
        return self._correo

    def __str__(self):
        return f"{self._nombre} ({self._correo})"
