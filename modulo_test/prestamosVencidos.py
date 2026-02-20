##REPORTE PRESTAMOS VENCIDOS
from Gestiones.herramientas import listaHerramientas
from Gestiones.GestionUsuarios import listarUsuarios
from Gestiones.GestionPrestamos import listaPrestamos
from Permisos.administrador import ingreso


def menuReporteVencidos(prestamos, datos):

    while True:
        print("\033[96m")
        print("""
        ╭─────────────────────────────────╮
                PRÉSTAMOS VENCIDOS    
        ╰─────────────────────────────────╯
            1 → Usuario
            2 → Administrador
            3 → Salir
            """)
        print("\033[0m")

        opcion= input("🎯 Seleccione su rol para continuar:").strip()
        if opcion =="1":
            print("Oops. No tienes permiso para ejecutar esta actividad.")
        elif opcion =="2":
            if ingreso(datos):
                reportePrestamosVencidos(prestamos):
        elif opcion =="3": 
            print("SALIENDO... ")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


#FUNCION PRESTAMOS VENCIDOS_____________________________________________________________________

def reportePrestamosVencidos(prestamos):

    prestamosActivos = []
    for i in prestamos["listaPrestamos"]:
        if i["estado"] == "activo":
            prestamosActivos.append(i)
    
    if not prestamosActivos:
        print("⚠️ No hay préstamos activos en este momento.")
        return

   while True:
        fechaDeHoy = input("📅 Ingrese la fecha de hoy(DD/MM/AAAA): ").strip()
            
        if len(fechaDeHoy) != 10:
            print("⚠️ Formato incorrecto. Debe ser DD/MM/AAAA (ej: 15/02/2026).")
            continue
            
        if fechaDeHoy[2] != "/" or fechaDeHoy[5] != "/":
            print("⚠️ Debe usar "/" para separar (DD/MM/AAAA). ")
            continue
        
        partes = fechaDeHoy.split("/")
            
        if len(partes) != 3:
            print("⚠️ Formato incorrecto.")
            continue
            
        dia = partes[0]
        mes = partes[1]
        anio = partes[2]
            
        if not dia.isdigit() or not mes.isdigit() or not anio.isdigit():
            print("⚠️ Día, mes y año deben ser números.")
            continue
        break

    
    prestamosActivos["estado"] = "activo"
    prestamosActivos["fechaDevolucion"] = fechaDevolucion
    prestamosActivos["observaciones"] = observaciones
        
    herramienta["cantidad disponible"] = int(disponible["cantidad disponible"]) - int(solicitudEncontrada["cantidadSolicitada"])
    guardarPrestamos(prestamos)
    print(f"✔️ Prestamo {idPrestamo} aprobado.")
    registrarLog(f"Prestamo aprobado: #{idPrestamo} - {solicitudEncontrada['idUsuario']} - {solicitudEncontrada['nombreHerramienta']}")

    print(f"→ FECHA LÍMITE: {fechaDevolucion}")




#DATETIME______________________________________________________________________________________________________

def prestamosVencidos(prestamos):
    from datetime import datetime

    fechaHoy = input("Ingrese la fecha de hoy (DD/MM/AAAA): ").strip()
    fechaHoyReal= datetime.strptime(fechaHoy, "%d/%m/%Y")

    vencidos = []

    for i in prestamos["listaPrestamos"]:
        if i["estado"] == "activo" and i.get("fechaDevolucion"):
            
            fechaDevReal= datetime.strptime(i["fechaDevolucion"], "%d/%m/%Y")

            if fechaDevReal < fechaHoyReal:
                vencidos.append(i)

    if not vencidos:
        print("⚠️ No hay préstamos vencidos.")
        return

    print("\033[95m")
    print(f"{'ID':<8} {'USUARIO':<20} {'HERRAMIENTA':<20}")
    print("─" * 55)
    
    for i in vencidos:
        print(f"{i['idPrestamo']:<8} {i['idUsuario']:<20} {i['nombreHerramienta']:<20}")
    
    print("=" * 55 + "\033[0m")  