#Gestón de vacaciones - Ferretería "La tuerca"

import csv
from datetime import datetime

# --- BASE DE DATOS ---
def cargar_empleados():
    empleados = {}
    with open("empleados.csv", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            empleados[fila["legajo"]] = {
                "nombre": fila["nombre"],
                "dias_disponibles": int(fila["dias_disponibles"]),
                "solicitudes": []
            }
    return empleados

# --- BUSCAR EMPLEADO ---
def buscar_empleado(legajo, empleados):
    if legajo in empleados:
        return empleados[legajo]
    return None

# --- CONSULTAR SALDO ---
def consultar_saldo(dias_disponibles, dias_solicitados):
    if dias_disponibles >= dias_solicitados:
        return True
    return False

# --- REGISTRAR SOLICITUD ---
def registrar_solicitud(legajo, empleados, fecha_inicio, fecha_fin, dias_solicitados):
    empleados[legajo]["solicitudes"].append({
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "dias": dias_solicitados
    })
    empleados[legajo]["dias_disponibles"] -= dias_solicitados

# --- NOTIFICAR ---
def notificar(mensaje):
    print(mensaje)

# --- MAIN ---
def main():
    empleados = cargar_empleados()
    
    print("=== Sistema de Gestión de Vacaciones ===")
    print("Ferretería La Tuerca")
    
    # 1. El empleado ingresa su legajo
    legajo = input("Ingrese su legajo: ").strip()
    if legajo == "" or not legajo.isdigit():
        notificar("Legajo inválido. Debe ingresar solo números.")
        return
    
    # 2. Gateway 1: ¿Existe el empleado?
    empleado = buscar_empleado(legajo, empleados)
    if empleado is None:
        notificar("Empleado no encontrado. Consulte con RRHH.")
        return
    
    print(f"Bienvenido/a, {empleado['nombre']}")
    print(f"Días disponibles: {empleado['dias_disponibles']}")

    # 3. El empleado ingresa fechas y días
    try:
        fecha_inicio = datetime.strptime(input("Ingrese la fecha de inicio (DD/MM/AAAA): ").strip(), "%d/%m/%Y")
    except ValueError:
        notificar("Fecha de inicio inválida. Debe ingresar el formato DD/MM/AAAA.")
        return
    
    try:
        fecha_fin = datetime.strptime(input("Ingrese la fecha de cierre (DD/MM/AAAA): ").strip(), "%d/%m/%Y")
    except ValueError:
        notificar("Fecha de cierre inválida. Debe ingresar el formato DD/MM/AAAA.")
        return
    
    try:
        dias = int(input("Ingrese la cantidad de días: "))
    except ValueError:
        notificar("Cantidad de días inválida. Debe ingresar un número.")
        return
    
    # 4. Gateway 2: ¿Tiene saldo suficiente?
    tiene_saldo = consultar_saldo(empleado["dias_disponibles"], dias)
    if tiene_saldo:
        registrar_solicitud(legajo, empleados, fecha_inicio, fecha_fin, dias)
        notificar("Solicitud exitosa. ¡Disfrute sus vacaciones!")
    else:
        notificar("Saldo insuficiente. No cuenta con suficientes días disponibles.")

if __name__ == "__main__":
    main()