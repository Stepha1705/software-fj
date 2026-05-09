from auth.auth_manager import AuthManager
from utils.time_manager import TimeManager
from services.servicio_sala import ServicioSala
from models.reserva import Reserva
from exceptions.errores import registrar_error, ErrorSistema

try:
    print("=== SISTEMA SOFTWARE FJ ===")

    auth = AuthManager()

    # Registro
    cliente = auth.registrar("Julissa", "julissa@mail.com", "1234")

    # Login
    cliente = auth.login("julissa@mail.com", "1234")

    # Tiempo automático
    horas = TimeManager.calcular_horas("08:00", "11:30")

    # Selección de sala
    servicio = ServicioSala("Sala Premium", horas)

    # Reserva
    reserva = Reserva(cliente, servicio)

    print(reserva.resumen())

except ErrorSistema as e:
    print("Ocurrió un error controlado del sistema.")
    registrar_error(str(e))

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
    registrar_error(f"Error inesperado: {e}")

