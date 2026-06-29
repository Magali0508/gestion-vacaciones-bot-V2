# Sistema de Gestión de Vacaciones — Ferretería "La Tuerca"

Bot de consola desarrollado en Python que automatiza el proceso de solicitud 
de vacaciones, eliminando la gestión manual a través de Recursos Humanos.

Trabajo Práctico Integrador — Organización Empresarial  
Tecnicatura Universitaria en Programación — UTN  
Integrantes: Magalí Tron, Pablo Kunz

---

## Descripción

El sistema permite a cada empleado:
- Consultar su saldo de días de vacaciones disponibles
- Solicitar un período de vacaciones ingresando fechas y cantidad de días
- Recibir confirmación o rechazo automático según las reglas de negocio

La lógica del bot responde fielmente al modelo de procesos BPMN 2.0 
diseñado para el trabajo, distinguiendo tareas del empleado y tareas 
automáticas del sistema.

---

## Requisitos

- Python 3.x (sin dependencias externas)

---

## Cómo ejecutar

1. Clonar el repositorio:
   git clone https://github.com/Magali0508/gestion-vacaciones-bot-V2

2. Asegurarse de que `empleados.csv` esté en la misma carpeta que `main.py`

3. Ejecutar:
   python main.py

---

## Archivos

| Archivo | Descripción |
|---|---|
| `main.py` | Lógica principal del bot (máquina de estados, validaciones, gateways) |
| `empleados.csv` | Base de datos simulada con legajo, nombre y días disponibles |

---

## Empleados de prueba

| Legajo | Nombre | Días disponibles |
|---|---|---|
| 1001 | Ana García | 15 |
| 1002 | Carlos López | 5 |
| 1003 | María Pérez | 0 |

---

## Flujo del proceso

1. El empleado ingresa su número de legajo
2. El sistema verifica si el legajo existe en la base de datos
3. Si existe, muestra nombre y saldo disponible
4. El empleado ingresa fecha de inicio, fecha de fin y cantidad de días
5. El sistema verifica si el saldo cubre los días solicitados
6. Si hay saldo suficiente, registra la solicitud
