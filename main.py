import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from auth.auth_manager import AuthManager
from utils.time_manager import TimeManager
from utils.logger import Logger

from services.servicio_sala import ServicioSala
from services.servicio_equipo import ServicioEquipo
from services.servicio_asesoria import ServicioAsesoria

from models.reserva import Reserva

print("=== SISTEMA SOFTWARE FJ ===")
print("Bienvenido al sistema\n")

try:

    auth = AuthManager()

   
    # DATOS CLIENTE
   

    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo: ")
    clave = input("Ingrese su contraseña: ")

    cliente = auth.registrar(nombre, correo, clave)

   
    # TIEMPO RESERVA
    

    hora_inicio = input("Hora inicio: ")
    hora_fin = input("Hora final: ")

    horas = TimeManager.calcular_horas(
        hora_inicio,
        hora_fin
    )

    
    # MENÚ SERVICIOS
    

    print("\nTIPOS DE SERVICIO")
    print("1. Reserva de Sala")
    print("2. Alquiler de Equipos")
    print("3. Asesoría")

    opcion = input("Seleccione una opción: ")

   
    # SERVICIO SALA
   

    if opcion == "1":

        print("\n1. Sala A")
        print("2. Sala B")
        print("3. Sala Premium")

        sala = input("Seleccione sala: ")

        if sala == "1":
            servicio = ServicioSala("Sala A", horas)

        elif sala == "2":
            servicio = ServicioSala("Sala B", horas)

        elif sala == "3":
            servicio = ServicioSala("Sala Premium", horas)

        else:
            raise ValueError("Sala inválida")

   
    # SERVICIO EQUIPO
    

    elif opcion == "2":

        print("\n1. Laptop")
        print("2. VideoBeam")
        print("3. Impresora")

        equipo = input("Seleccione equipo: ")

        if equipo == "1":
            servicio = ServicioEquipo("Laptop", horas)

        elif equipo == "2":
            servicio = ServicioEquipo("VideoBeam", horas)

        elif equipo == "3":
            servicio = ServicioEquipo("Impresora", horas)

        else:
            raise ValueError("Equipo inválido")

  
    # SERVICIO ASESORIA
   

    elif opcion == "3":

        print("\n1. Programación")
        print("2. Bases de Datos")
        print("3. Redes")

        asesoria = input("Seleccione asesoría: ")

        if asesoria == "1":
            servicio = ServicioAsesoria("Programación", horas)

        elif asesoria == "2":
            servicio = ServicioAsesoria("Bases de Datos", horas)

        elif asesoria == "3":
            servicio = ServicioAsesoria("Redes", horas)

        else:
            raise ValueError("Asesoría inválida")

    else:
        raise ValueError("Servicio no válido")

  
    # CREACIÓN DE RESERVA
    

    reserva = Reserva(cliente, servicio)

    print("\n=== RESERVA GENERADA ===")
    print(reserva.resumen())

    Logger.registrar_evento(
        "Reserva realizada correctamente"
    )

except Exception as e:

    print(f"\nERROR: {e}")

    Logger.registrar_error(str(e))

finally:
    print("\nSistema finalizado")