from Permisos.usuarios import cargarPrestamos, guardarPrestamos
from Otros.Logs import registrarLog

def menuGestionPrestamos(datos, inventario, prestamos):
    prestamos = cargarPrestamos()
    
    while True:
        print("\033[38;5;213m") 
        print("""
        ----------------------------------
                GESTIÓN PRÉSTAMOS
        ----------------------------------

            
        1 → Solicitudes pendientes
        2 → Aprobar solicitud
        3 → Registrar devolución
        4 → Guardar y salir
        \033[0m""")
        print()

        opcion = input("🎯 Seleccione la opción que desea ejecutar: ").strip()

        if opcion=="1":
            solicitudesPendientes(prestamos)
        elif opcion=="2":
            aprobarPrestamo(inventario, prestamos)
        elif opcion=="3":
            regitrarDevolucion(inventario, prestamos)
        elif opcion=="4":
            guardarPrestamos(prestamos)
            print("""✔️ La información ha sido guardada con exito. 
                Saliendo... Vuelva pronto.""")            
            break
        else:
            print("⚠️ Opción inválida. Intente nuevamente.")

        input("Presione cualquier tecla para continuar...")

#SOLICITUDES PENDIENTES
def solicitudesPendientes(prestamos):
    print("""\033[3m
        SOLICITUDES PENDIENTES
    ----------------------------
    \033[0m""")

    pendientes = []
    for solicitud in prestamos["listaPrestamos"]:
        if solicitud["estado"] == "pendiente":
            pendientes.append(solicitud)
    
    if not pendientes:
        print("⚠️ No hay solicitudes pendientes en este momento.\n")
        return
        
    print(f"{'ID':<8} {'USUARIO':<15} {'HERRAMIENTA':<20} {'CANT':<8} {'ESTADO':<12} {'ID_HERR':<10}")
    print("─" * 80)

    for solicitud in pendientes:
        print(f"{solicitud['idPrestamo']:<8} "
            f"{solicitud['idUsuario']:<15} "
            f"{solicitud['nombreHerramienta']:<20} "
            f"{solicitud['cantidadSolicitada']:<8} "
            f"{solicitud['estado']:<12} "
            f"{solicitud['idHerramienta']:<10}"
        )

    print("─" * 80)
    print(f"✔️ TOTAL: {len(pendientes)} solicitud(es) pendiente(s).")

#APROBAR PRESTAMO:____________________________________________________________

def aprobarPrestamo(inventario, prestamos):
    print("""\033[3m
        APROBAR PRÉSTAMOS
    ----------------------------
    \033[0m""")

    pendientes = []
    for solicitud in prestamos["listaPrestamos"]:
        if solicitud["estado"] == "pendiente":
            pendientes.append(solicitud)
    
    if not pendientes:
        print("⚠️ No hay solicitudes pendientes en este momento.\n")
        return
    
    idPrestamo= input("🆔 Ingrese el ID del préstamo que desea aprobar:")
    solicitudEncontrada = None
    for solicitud in prestamos["listaPrestamos"]:
        if solicitud["idPrestamo"] == idPrestamo and solicitud["estado"] == "pendiente":
            solicitudEncontrada = solicitud
            break
    
    if not solicitudEncontrada:
        print("⚠️ Solicitud de préstamo no encontrada.\n")
        return
    
    disponible = None
    for herramienta in inventario["listaHerramientas"]:
        if herramienta["idHerramienta"] == solicitudEncontrada["idHerramienta"]:
            disponible = herramienta
        
    if int(disponible["cantidad disponible"]) < int(solicitudEncontrada["cantidadSolicitada"]):
        print(f"⚠️ No hay suficientes unidades disponibles de esta herramienta.\n")
        registrarLog(f"ERROR: Intento aprobar prestamo sin stock. ID: {idPrestamo}, Herramienta: {solicitudEncontrada['nombreHerramienta']}, Solicitadas: {solicitudEncontrada['cantidad']}, Disponibles: {disponible['cantidad disponible']}")
        print(f"   Solicitadas: {solicitudEncontrada['cantidadSolicitada']}, Disponibles: {disponible['cantidad disponible']}")
        return
    

    while True:
        fechaDeHoy =input("📅  Ingrese la fecha de hoy (inicio del préstamo): (DD/MM/AAAA):").strip()

         if len(fechaDeHoy) != 10:
            print("⚠️ Formato incorrecto. Debe ser DD/MM/AAAA (ej: 15/02/2026)")
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

#_________________________________________________
        fechaDevolucion = input("📅 Ingrese la fecha límite de devolución (DD/MM/AAAA): ").strip()
            
        if len(fechaDevolucion) != 10:
            print("⚠️ Formato incorrecto. Debe ser DD/MM/AAAA (ej: 15/02/2026)")
            continue
            
        if fechaDevolucion[2] != "/" or fechaDevolucion[5] != "/":
            print("⚠️ Debe usar "/" para separar (DD/MM/AAAA). ")
            continue
        
        partes = fechaDevolucion.split("/")
            
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

    observaciones = input("(OPCIONAL) Observaciones:").strip().lower()
    
    solicitudEncontrada["estado"] = "activo"
    solicitudEncontrada["fechaDevolucion"] = fechaDevolucion
    solicitudEncontrada["observaciones"] = observaciones
        
    herramienta["cantidad disponible"] = int(disponible["cantidad disponible"]) - int(solicitudEncontrada["cantidadSolicitada"])
    guardarPrestamos(prestamos)
    print(f"✔️ Prestamo {idPrestamo} aprobado.")
    registrarLog(f"Prestamo aprobado: #{idPrestamo} - {solicitudEncontrada['idUsuario']} - {solicitudEncontrada['nombreHerramienta']}")
    print(f"→ FECHA LÍMITE: {fechaDevolucion}")

#REGISTRAR DEVOLUCIÓN:__________________________________________________________

def regitrarDevolucion(inventario, prestamos):

    print("""\033[3m
        REGISTRAR DEVOLUCIÓN
    ----------------------------
    \033[0m""")

    prestamosActivos = []
    for i in prestamos["listaPrestamos"]:
        if i["estado"] == "activo":
            prestamosActivos.append(i)
    
    if not prestamosActivos:
        print("⚠️ No hay préstamos activos en este momento.")
        return
    
    print("\033[96m" + "=" * 55)
    print("📌 PRÉSTAMOS ACTIVOS".center(55))
    print("=" * 55)

    for i in prestamosActivos:
        print("-" * 55)
        print(f"🔹 ID Préstamo: {i['idPrestamo']}")
        print(f"   Usuario: {i['idUsuario']}")
        print(f"   Herramienta: {i['nombreHerramienta']}")
        print(f"   Cantidad: {i['cantidadSolicitada']}")
        print(f"   Fecha límite: {i['fechaDevolucion']}")
        print("-" * 55)

    print("=" * 55)
    print(f"📊 TOTAL ACTIVOS: {len(prestamosActivos)}")
    print("=" * 55 + "\033[0m")

    idPrestamo = input("🆔 Ingrese el ID del préstamo a devolver: ").strip()

    prestamoEncontrado = None
    for hallado in prestamos["listaPrestamos"]:
        if hallado["idPrestamo"] == idPrestamo and hallado["estado"] == "activo":
            prestamoEncontrado = hallado

    if not prestamoEncontrado:
        print(f"⚠️ No hay encontró préstamo con el ID {idPrestamo}.")
        return
    
    confirmar = input("👀¿Está seguro que registrará devolución de este préstamo? (si/no): ").lower().strip()
        
    if confirmar == 'si':
        prestamoEncontrado["estado"] = "devuelto"
    else:
        print(" ⚠️ Proceso cancelado.")
        return
    
    for cantidadNueva in inventario["listaHerramientas"]:
        if cantidadNueva["idHerramienta"] == cantidadNueva["idHerramienta"]:
            cantidadNueva["cantidad disponible"] = int(cantidadNueva["cantidad disponible"]) + int(prestamoEncontrado["cantidadSolicitada"])
            break
    guardarPrestamos(prestamos, inventario)
    print(f"✔️ Herramienta '{prestamoEncontrado['nombreHerramienta']}' devuelta exitosamente.")
    registrarLog(f"Devolucion registrada: Prestamo #{idPrestamo} - {prestamoEncontrado['nombreHerramienta']}")

    
