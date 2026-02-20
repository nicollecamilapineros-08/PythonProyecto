#ACTIVIDADES USUARIO--------------------------------------------

from Gestiones.herramientas import listarHerramientas, buscarHerramienta
from Otros.Logs import registrarLog
import json

def cargarPrestamos(nom_archivo="registroPrestamos.json"):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
            prestamos = {
    "listaPrestamos": [
        {
            "idPrestamo": "001",
            "idUsuario": "002",
            "idHerramienta": "01",  
            "nombreHerramienta": "Taladro",
            "fechaPrestamo": "2024-02-10",
            "estado": "activo", 
            "cantidadSolicitada": 2
        }
    ]
}
    guardarPrestamos(prestamos)
    return prestamos
    
def guardarPrestamos(prestamo, nom_archivo="registroPrestamos.json"):
    try:
        with open(nom_archivo, "w") as arch:
            json.dump(prestamo, arch, indent=4)
    except Exception:
        prestamo = {}
        print("✔️ Informacion guardada exitosamente.")

#--------------------------------------------------------------

def menuUsuario(inventario, prestamos):

    while True:
        print("\033[96m")
        print("""
            ╭─────────────────────────────────╮
                        MENÚ USUARIO                                     
            ╰─────────────────────────────────╯
            1 → Ver todas las herramientas
            2 → Consultar estado de herramienta
            3 → Crear solicitud de herramienta
            4 → Estado de mis solicitudes
            5 → Guardar y salir
                """)
        print("\033[0m")

        opcion= input("🎯 Selecciona la opción que deseas ejecutar:").strip()

        if opcion == "1":
            listarHerramientas(inventario)
        elif opcion == "2":
            buscarHerramienta(inventario)
        elif opcion == "3":
            crearSolicitud(inventario, prestamos)
        elif opcion == "4":
            prestamosActuales(prestamos)
        elif opcion == "5":
            print("""✔️ La información ha sido guardada con exito. 
                Saliendo... Vuelva pronto.""")
            break
        else:
            print("⚠️  Opción inválida. Intente nuevamente.")
        input("Presione cualquier tecla para continuar...")


#CREAR SOLICITUD________________________________________________

def crearSolicitud(inventario, prestamos):
 

    #DISPONIBILIDAD CANTIDAD Y ESTADO ACTIVA:

    disponible = []
    for herramienta in inventario["listaHerramientas"]:
        if int(herramienta["cantidad disponible"]) > 0:
            if herramienta["estado"] == "activa":
                disponible.append(herramienta)
    
    if not disponible:
        print("⚠️ No hay herramientas disponibles para solicitar.")
        return
    
    print("\033[95m" + "=" * 55)
    print("🛠️ HERRAMIENTAS DISPONIBLES".center(55))
    print("=" * 55)

    for herramienta in disponible:
        print("-" * 55)
        print(f"🔹 ID: {herramienta['idHerramienta']}")
        print(f"   Nombre: {herramienta['nombre']}")
        print(f"   Cantidad disponible: {herramienta['cantidad disponible']} unidades")
    print("-" * 55)
    print("=" * 55 + "\033[0m")     
        

    idHerramienta = input("🆔 Ingrese ID de la herramienta a solicitar: ").strip()

    #BUSCA HERRAMIENTA EN INVENTARIO:

    herramientaEncontrada = None
    for herramienta in inventario["listaHerramientas"]:
        if herramienta["idHerramienta"] == idHerramienta:
            herramientaEncontrada = herramienta
            break
    
    if not herramientaEncontrada:
        print(f"⚠️ La herramienta con ID {idHerramienta} no fue encontrada.")
        return
    
    #DISPONIBILIDAD CANTIDAD:

    if int(herramientaEncontrada["cantidad disponible"]) <= 0:
        print("⚠️ Unidades insuficientes. ")
        return

    if herramientaEncontrada["estado"] != "activa":
        print(f"⚠️ La herramienta se encuentra {herramientaEncontrada['estado']} actualmente. ")
        return

    #CANTIDAD A SOLICITAR:

    while True: 
        cantidadSolicitada= input("🎯Ingrese la cantidad que desea solicitar:")
        if cantidadSolicitada> 0 and cantidadSolicitada<= int(herramientaEncontrada["cantidad disponible"]):
            break
        print("⚠️ Cantidad inválida. Intente nuevamente.")
        if cantidadSolicitada.isdigit():
            cantidadSolicitada = int(cantidadSolicitada)

    observaciones = input("📝 (OPCIONAL) Observaciones: ").strip()

    #NUEVO ID PARA EL PRÉSTAMO:

    idPrestamo = str(len(prestamos["listaPrestamos"]) + 1)
    idUsuario = input("🆔 Ingrese su ID para continuar con la operación: ").strip()

    nuevaSolicitud = {
        "idPrestamo": idPrestamo,
        "nombre": idUsuario["nombre"],
        "apellido": idUsuario["apellido"],
        "idUsuario": idUsuario
        "idHerramienta": idHerramienta,
        "nombreHerramienta": herramientaEncontrada["nombre"],
        "cantidadSolicitada": cantidadSolicitada,
        "fechaDeInicio": "",
        "fechaDevolucion": "",  
        "estado": "pendiente",  
        "observaciones": observaciones
    }
    prestamos["listaPrestamos"].append(nuevaSolicitud)
    guardarPrestamos(prestamos)
    registrarLog(f"Solicitud creada: #{idPrestamo} - {idUsuario} solicita {herramientaEncontrada['nombre']}")


    print("\n" + "─" * 70)
    print("✅ SOLICITUD CREADA EXITOSAMENTE")
    print("─" * 70)
    print("→ Estado: Pendiente de aprobación.")
    print("→ Su solicitud será revisada por el administrador.")
    print("→ Puede consultar el estado en 'Estado de mis solicitudes'.")
    print("─" * 70)

#VER PRESTAMOS DEL USUARIO___________________________________________________

def prestamosActuales( prestamos):

 
    #FILTRAR PRÉSTAMOS DEL USUARIO:
    idUsuario = input("🆔 Ingrese su ID para continuar con la operación: ").strip()

    prestamosActuales = []
    for i in prestamos["listaPrestamos"]:
        if i["idUsuario"] == idUsuario:
            prestamosActuales.append(i)
    
    if not prestamosActuales:
        print("⚠️ Actualmente no tiene prestamos / solicitudes. ")
        return
    
    print("\033[96m" + "=" * 50)
    print("REGISTRO".center(50))
    print("=" * 50)

    print(f"{'ID':<8} {'HERRAMIENTA':<20} {'CANTIDAD':<10} {'ESTADO':<12}")
    print("-" * 50)

    for i in prestamosActuales:
        print(f"{i['idPrestamo']:<8} "
            f"{i['nombreHerramienta']:<20} "
            f"{i['cantidadSolicitada']:<10} "
            f"{i['estado']:<12}")

    print("-" * 50)
    print(f"📊 TOTAL: {len(prestamosActuales)} solicitud(es)")
    print("=" * 50)
    print("\033[0m")