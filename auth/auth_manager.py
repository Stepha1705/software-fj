from models.cliente import Cliente
from exceptions.errores import ErrorSistema


class AuthManager:
    def __init__(self):
        self._usuarios = {}

    def registrar(self, nombre, correo, password):
        if correo in self._usuarios:
            raise ErrorSistema("Usuario ya registrado")

        cliente = Cliente(nombre, correo)
        self._usuarios[correo] = {
            "cliente": cliente,
            "password": password
        }
        return cliente

    def login(self, correo, password):
        if correo not in self._usuarios:
            raise ErrorSistema("Usuario no existe")

        if self._usuarios[correo]["password"] != password:
            raise ErrorSistema("Contraseña incorrecta")

        return self._usuarios[correo]["cliente"]
    