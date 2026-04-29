import sys
import os

# Añade la raíz del proyecto al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from auth.auth_manager import AuthManager
from utils.time_manager import TimeManager
from services.servicio_sala import ServicioSala
from models.reserva import Reserva

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
