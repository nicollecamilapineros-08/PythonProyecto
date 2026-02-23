##REPORTE PRESTAMOS VENCIDOS

import json

def cargar_prestamos():
    archivo = open("registroPrestamos.json", "r", encoding="utf-8")
    prestamos = json.load(archivo)
    archivo.close()
    return prestamos

def cargar_herramientas():
    archivo = open("registroHerramientas.json", "r", encoding="utf-8")
    inventario = json.load(archivo)
    archivo.close()
    return inventario

def cargar_usuarios():
    archivo = open("registroUsuarios.json", "r", encoding="utf-8")
    usuarios = json.load(archivo)
    archivo.close()
    return usuarios


prestamos = cargar_prestamos()
inventario = cargar_herramientas()
usuarios =cargar_usuarios()

    
for p in prestamos["listaPrestamos"]:
    id_herramienta = p["idHerramienta"]
    nombre_herramienta = p["nombreHerramienta"]
    fecha_devolucion = p["fechaDevolucion"]
        




#FUNCION PRESTAMOS VENCIDOS_________________________

def reportePrestamosVencidos(prestamos):
    prestamito = cargar_prestamos(prestamos)
    inventarito = cargar_herramientas(inventario)

    print("Reporte de préstamos vencidos:")

    prestamosActivos = []
    for i in prestamito["listaPrestamos"]:
        if i["estado"] == "activo":
            prestamosActivos.append(i)
    
    if not prestamosActivos:
        print("⚠️ No hay préstamos activos en este momento.")
        return

    while True:
        fechaActual = input("📅 Ingrese la fecha de hoy(DD/MM/AAAA): ").strip()
            
        if len(fechaActual) != 10:
            print("⚠️ Formato incorrecto. Debe ser DD/MM/AAAA (ej: 15/02/2026).")
            continue
            
        if fechaActual[2] != "/" or fechaActual[5] != "/":
            print("⚠️ Debe usar "/" para separar (DD/MM/AAAA). ")
            continue
        
        partes = fechaActual.split("/")
            
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

    prestamosVencidos = []
    for prestamo in prestamosActivos:
        fechaDevolucion = prestamo.get("fechaDevolucion")
        if fechaDevolucion < fechaActual:
            prestamosVencidos.append(prestamo)
             

    if not prestamosVencidos:
        print("No hay préstamos vencidos en este momento.")

    try:
        #TOTAL DE DIAS VENCIDOS
            partes_dev = fechaDevolucion.split("/")
            partes_hoy = fechaActual.split("/")
            
            diasDev = int(partes_dev[0])
            mesDev = int(partes_dev[1])
            anioDev = int(partes_dev[2])
            
            diaActual = int(partes_hoy[0])
            mesActual = int(partes_hoy[1])
            anioActual = int(partes_hoy[2])
            
            # Cálculo aproximado
            dias_anio = (anioActual - anioDev) * 365
            dias_mes = (mesActual - mesDev) * 30
            dias_dia = diaActual - diasDev
            
            total = dias_anio + dias_mes + dias_dia
            
            return total if total > 0 else 0
    except Exception as e:
        print(f"Error al calcular días vencidos: {e}")
        return 0
    
def generar_reporte_markdown(prestamos_vencidos, fecha_actual):
    with open("reporte_prestamos_vencidos.md", "w", encoding="utf-8") as archivo:
        archivo.write("# 📋 Reporte de Préstamos Vencidos\n\n")
        archivo.write(f"**Fecha de generación:** {fecha_actual}\n\n")

        if not prestamos_vencidos:
            archivo.write("No hay préstamos vencidos.\n")
            return

        archivo.write("| ID Herramienta | Usuario | Fecha Devolución | Estado |\n")
        archivo.write("|---------------|----------|------------------|--------|\n")

        for p in prestamos_vencidos:
            archivo.write(
                f"| {p['idHerramienta']} | {p['usuario']} | {p['fechaDevolucion']} | {p['estado']} |\n"
            )

    print("✅ Reporte generado correctamente en formato Markdown.")



#__________________________
def menuReporteVencidos(prestamos):

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
            reportePrestamosVencidos(prestamos)
        elif opcion =="3": 
            print("SALIENDO... ")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
menuReporteVencidos(prestamos)

##from Permisos.administrador import ingreso
##  if ingreso(datos):reportePrestamosVencidos(prestamos)
