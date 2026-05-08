# main.py interactivo para reservas


import sys
import os

# Añade la raíz del proyecto al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from auth.auth_manager import AuthManager
from utils.time_manager import TimeManager
from services.servicio_sala import ServicioSala
from models.reserva import Reserva

print("=== SISTEMA SOFTWARE FJ ===")
print("Bienvenido al sistema de reservas\n")

# Instancia del sistema de autenticación
auth = AuthManager()


# INGRESO DE DATOS USUARIO


nombre = input("Ingrese su nombre: ")
correo = input("Ingrese su correo: ")
clave = input("Ingrese su contraseña: ")

print("\n=== DATOS DE LA RESERVA ===")

hora_inicio = input("Hora de inicio (Ejemplo 08:00): ")
hora_fin = input("Hora final (Ejemplo 11:30): ")

print("\nTipos de sala disponibles:")
print("1. Sala Básica")
print("2. Sala Premium")
print("3. Sala VIP")

opcion = input("Seleccione una opción: ")


# VALIDACIÓN DE SALA


if opcion == "1":
    tipo_sala = "Sala A"
elif opcion == "2":
    tipo_sala = "Sala B"
elif opcion == "3":
    tipo_sala = " Sala Premium"
else:
    print("Opción inválida. Se asignará Sala A")
    tipo_sala = "Sala A"


# REGISTRO Y LOGIN

cliente = auth.registrar(nombre, correo, clave)
cliente = auth.login(correo, clave)


# CÁLCULO DE HORAS


horas = TimeManager.calcular_horas(hora_inicio, hora_fin)

# CREACIÓN DEL SERVICIO


servicio = ServicioSala(tipo_sala, horas)


# CREACIÓN DE LA RESERVA

reserva = Reserva(cliente, servicio)


# RESULTADO FINAL


print("\n=== RESERVA GENERADA ===")
print(reserva.resumen())

print("\nGracias por usar SOFTWARE FJ")

