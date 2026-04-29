


#
# Sistema Integral de Gestión de Clientes, Servicios y Reservas
# Empresa: Software FJ


from abc import ABC, abstractmethod
from datetime import datetime



# ARCHIVO DE LOGS


LOG_FILE = "logs_software_fj.txt"


def registrar_log(mensaje):
    """Registra eventos y errores en un archivo de logs."""
    with open(LOG_FILE, "a", encoding="utf-8") as archivo:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"[{fecha}] {mensaje}\n")


# EXCEPCIONES PERSONALIZADAS


class ErrorSistema(Exception):
    """Excepción general del sistema."""
    pass


class ErrorCliente(ErrorSistema):
    """Error relacionado con datos del cliente."""
    pass


class ErrorServicio(ErrorSistema):
    """Error relacionado con servicios."""
    pass


class ErrorReserva(ErrorSistema):
    """Error relacionado con reservas."""
    pass



# CLASE ABSTRACTA GENERAL


class EntidadSistema(ABC):
    """Clase abstracta general para entidades del sistema."""

    @abstractmethod
    def obtener_informacion(self):
        pass



# CLASE CLIENTE


class Cliente(EntidadSistema):
    """Representa un cliente con datos encapsulados y validados."""

    def __init__(self, nombre, documento, correo):
        try:
            if not nombre or len(nombre.strip()) < 3:
                raise ErrorCliente("El nombre del cliente no es válido.")

            if not documento or not documento.isdigit():
                raise ErrorCliente("El documento debe contener solo números.")

            if "@" not in correo or "." not in correo:
                raise ErrorCliente("El correo electrónico no es válido.")

            self.__nombre = nombre
            self.__documento = documento
            self.__correo = correo

            registrar_log(f"Cliente registrado correctamente: {nombre}")

        except ErrorCliente as error:
            registrar_log(f"Error al registrar cliente: {error}")
            raise

    def obtener_nombre(self):
        return self.__nombre

    def obtener_documento(self):
        return self.__documento

    def obtener_correo(self):
        return self.__correo

    def obtener_informacion(self):
        return f"Cliente: {self.__nombre} | Documento: {self.__documento} | Correo: {self.__correo}"



# CLASE ABSTRACTA SERVICIO


class Servicio(EntidadSistema):
    """Clase abstracta para los servicios ofrecidos por Software FJ."""

    def __init__(self, nombre, valor_hora, disponible=True):
        if valor_hora <= 0:
            raise ErrorServicio("El valor por hora debe ser mayor que cero.")

        self._nombre = nombre
        self._valor_hora = valor_hora
        self._disponible = disponible

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass

    def obtener_informacion(self):
        estado = "Disponible" if self._disponible else "No disponible"
        return f"Servicio: {self._nombre} | Valor hora: ${self._valor_hora} | Estado: {estado}"

    def esta_disponible(self):
        return self._disponible



# SERVICIO 1: RESERVA DE SALA


class ReservaSala(Servicio):
    def __init__(self):
        super().__init__("Reserva de Sala", 50000)

    def validar_parametros(self, duracion):
        if duracion <= 0:
            raise ErrorServicio("La duración de la reserva debe ser mayor que cero.")
        if duracion > 8:
            raise ErrorServicio("Una sala no puede reservarse por más de 8 horas.")

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)
        subtotal = duracion * self._valor_hora
        total = subtotal + (subtotal * impuesto / 100) - (subtotal * descuento / 100)
        return max(total, 0)



# SERVICIO 2: ALQUILER DE EQUIPOS


class AlquilerEquipo(Servicio):
    def __init__(self):
        super().__init__("Alquiler de Equipo", 70000)

    def validar_parametros(self, duracion):
        if duracion <= 0:
            raise ErrorServicio("La duración del alquiler debe ser mayor que cero.")
        if duracion > 12:
            raise ErrorServicio("El alquiler de equipos no puede superar 12 horas.")

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)

        # Polimorfismo: cálculo diferente al de sala
        subtotal = duracion * self._valor_hora

        # Cargo adicional por mantenimiento del equipo
        cargo_mantenimiento = 15000

        total = subtotal + cargo_mantenimiento
        total = total + (total * impuesto / 100) - (total * descuento / 100)

        return max(total, 0)


# SERVICIO 3: ASESORÍA ESPECIALIZADA


class AsesoriaEspecializada(Servicio):
    def __init__(self):
        super().__init__("Asesoría Especializada", 120000)

    def validar_parametros(self, duracion):
        if duracion <= 0:
            raise ErrorServicio("La duración de la asesoría debe ser mayor que cero.")
        if duracion > 6:
            raise ErrorServicio("La asesoría no puede superar 6 horas.")

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)

        # Polimorfismo: cálculo propio para asesorías
        subtotal = duracion * self._valor_hora

        # Si dura más de 3 horas, se aplica un recargo técnico
        if duracion > 3:
            subtotal += 30000

        total = subtotal + (subtotal * impuesto / 100) - (subtotal * descuento / 100)

        return max(total, 0)



# CLASE RESERVA


class Reserva:
    """Integra cliente, servicio, duración y estado."""

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        try:
            if not self.servicio.esta_disponible():
                raise ErrorReserva("El servicio no está disponible.")

            self.servicio.validar_parametros(self.duracion)
            self.estado = "Confirmada"
            registrar_log(f"Reserva confirmada para {self.cliente.obtener_nombre()} - {self.servicio._nombre}")

        except ErrorServicio as error:
            registrar_log(f"Error al confirmar reserva: {error}")
            raise ErrorReserva("No se pudo confirmar la reserva.") from error

    def cancelar(self):
        try:
            if self.estado == "Cancelada":
                raise ErrorReserva("La reserva ya se encuentra cancelada.")

            self.estado = "Cancelada"
            registrar_log(f"Reserva cancelada para {self.cliente.obtener_nombre()}")

        except ErrorReserva as error:
            registrar_log(f"Error al cancelar reserva: {error}")
            raise

    def procesar(self, impuesto=19, descuento=0):
        """Procesa la reserva y calcula el costo final."""
        try:
            if self.estado != "Confirmada":
                raise ErrorReserva("La reserva debe estar confirmada antes de procesarse.")

            costo = self.servicio.calcular_costo(self.duracion, impuesto, descuento)

        except ErrorReserva as error:
            registrar_log(f"Error de reserva: {error}")
            raise

        except ErrorServicio as error:
            registrar_log(f"Error de servicio durante el procesamiento: {error}")
            raise ErrorReserva("No fue posible procesar la reserva.") from error

        else:
            self.estado = "Procesada"
            registrar_log(f"Reserva procesada. Total: ${costo}")
            return costo

        finally:
            registrar_log("Finalizó intento de procesamiento de reserva.")

    def obtener_informacion(self):
        return (
            f"{self.cliente.obtener_nombre()} | "
            f"{self.servicio._nombre} | "
            f"Duración: {self.duracion} horas | "
            f"Estado: {self.estado}"
        )



# SISTEMA PRINCIPAL


class SistemaSoftwareFJ:
    """Sistema principal con listas internas."""

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def agregar_cliente(self, nombre, documento, correo):
        try:
            cliente = Cliente(nombre, documento, correo)

        except ErrorCliente as error:
            print(f"Error cliente: {error}")

        else:
            self.clientes.append(cliente)
            print("Cliente agregado correctamente.")

        finally:
            registrar_log("Finalizó operación de registro de cliente.")

    def agregar_servicio(self, servicio):
        try:
            if not isinstance(servicio, Servicio):
                raise ErrorServicio("El objeto no corresponde a un servicio válido.")

            self.servicios.append(servicio)
            registrar_log(f"Servicio agregado: {servicio._nombre}")
            print("Servicio agregado correctamente.")

        except ErrorServicio as error:
            registrar_log(f"Error al agregar servicio: {error}")
            print(f"Error servicio: {error}")

    def crear_reserva(self, cliente, servicio, duracion):
        try:
            if cliente not in self.clientes:
                raise ErrorReserva("El cliente no está registrado en el sistema.")

            if servicio not in self.servicios:
                raise ErrorReserva("El servicio no está registrado en el sistema.")

            reserva = Reserva(cliente, servicio, duracion)
            reserva.confirmar()
            self.reservas.append(reserva)

        except ErrorReserva as error:
            registrar_log(f"Error al crear reserva: {error}")
            print(f"Error reserva: {error}")

        else:
            print("Reserva creada y confirmada correctamente.")

        finally:
            registrar_log("Finalizó operación de creación de reserva.")

    def mostrar_clientes(self):
        print("\n--- CLIENTES REGISTRADOS ---")
        for cliente in self.clientes:
            print(cliente.obtener_informacion())

    def mostrar_servicios(self):
        print("\n--- SERVICIOS DISPONIBLES ---")
        for servicio in self.servicios:
            print(servicio.obtener_informacion())

    def mostrar_reservas(self):
        print("\n--- RESERVAS ---")
        for reserva in self.reservas:
            print(reserva.obtener_informacion())



# SIMULACIÓN DE 10 OPERACIONES COMPLETAS

def simulacion():
    sistema = SistemaSoftwareFJ()

    print("\n===== SISTEMA SOFTWARE FJ =====\n")

    # 1. Registrar cliente válido
    sistema.agregar_cliente("Cristian Méndez", "1012345678", "cristian@email.com")

    # 2. Registrar cliente válido
    sistema.agregar_cliente("Laura Gómez", "1020304050", "laura@email.com")

    # 3. Registrar cliente inválido
    sistema.agregar_cliente("Jo", "ABC123", "correo_invalido")

    # 4. Crear servicios válidos
    sala = ReservaSala()
    equipo = AlquilerEquipo()
    asesoria = AsesoriaEspecializada()

    sistema.agregar_servicio(sala)

    # 5. Agregar otro servicio válido
    sistema.agregar_servicio(equipo)

    # 6. Agregar tercer servicio válido
    sistema.agregar_servicio(asesoria)

    # 7. Intentar agregar servicio incorrecto
    sistema.agregar_servicio("Servicio no válido")

    # 8. Crear reserva exitosa
    sistema.crear_reserva(sistema.clientes[0], sala, 2)

    # 9. Crear reserva fallida por duración inválida
    sistema.crear_reserva(sistema.clientes[1], asesoria, 10)

    # 10. Procesar reserva exitosa
    try:
        reserva = sistema.reservas[0]
        total = reserva.procesar(impuesto=19, descuento=10)
        print(f"\nReserva procesada correctamente. Total a pagar: ${total:.2f}")

    except ErrorReserva as error:
        print(f"Error al procesar reserva: {error}")

    # Operaciones adicionales para mostrar estabilidad
    sistema.mostrar_clientes()
    sistema.mostrar_servicios()
    sistema.mostrar_reservas()

    print("\nLa simulación finalizó. Revise el archivo logs_software_fj.txt")



# EJECUCIÓN PRINCIPAL


if __name__ == "__main__":
    simulacion()