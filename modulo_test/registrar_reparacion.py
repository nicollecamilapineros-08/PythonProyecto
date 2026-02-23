
import json

def cargarReparaciones(nom_archivo="cargarReparaciones.json"):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
            enReparacion = { 
                "listaHerramientas": [
            {
            "idHerramienta": "02",
            "nombre": "Pala",
            "estado": "en reparacion",
            "fechaInicio": "20-02-2026",
            "fechaEstimadaFin": "23-02-2026",
            "observaciones": ""
        },
        {
            "idHerramienta": "02",
            "nombre": "Pala",
            "estado": "en reparacion",
            "fechaInicio": "20-02-2026",
            "fechaEstimadaFin": "23-02-2026",
            "observaciones": ""

        }
        ]
        }

def guardarReparaciones(reparaciones, nom_archivo="cargarReparaciones.json"):
    try:
        with open(nom_archivo, "w") as arch:
            json.dump(reparaciones, arch, indent=4)
    except Exception:
        reparaciones = {}
        print("✔️ Informacion guardada exitosamente.")

def cargarHerramientas(inventario):
    archivo = open("registroHerramientas.json", "r", encoding="utf-8")
    inventario = json.load(archivo)
    archivo.close()
    return inventario


def controlReparacion(inventario):
    cargarHerramientas(inventario)

    print("""\033[3m
      HERRAMIENTAS ACTIVAS
    -------------------------
    \033[0m""")


    #VERIFICA SI HAY INVENTARIO_________________________________________

    herramientasDisponibles = []
    for i in inventario['ListaHerramientas']:
        if i["estado"] == "activa":
            herramientasDisponibles.append(i)

    if not herramientasDisponibles:
        print("⚠️ No hay herramientas activas en este momento.")
        return
    
    print(f"{'ID':<8} {'NOMBRE':<25} {'ESTADO':<20}")
    print("─" * 50)

    for herramienta in inventario["listaHerramientas"]:
        print(f"{herramienta['idHerramienta']:<8} "
              f"{herramienta['nombre']:<25} "
              f"{herramienta['estado']:<20} ")
   
    
    print("─" * 50)
    print(f"✔️  Total de herramientas activas: {len(inventario['listaHerramientas'])}")

    #PIDE FECHA INICIO_________________________________________

    while True:
        idHerramientaEditar= input("Ingrese el ID de la herramienta a enviar a reparación:").strip()
        if idHerramientaEditar in herramientasDisponibles:
            continue
        print("Herramienta inválida. Intente nuevamente.")
    
        inicioReparacion=input("Ingrese la fecha de inicio de la reparación (ejemplo: 15-01-2026):")
        if len(inicioReparacion) != 10:
            print("⚠️ Formato incorrecto. Debe ser DD/MM/AAAA (ej: 15-01-2026)")
            continue
                
        if inicioReparacion[2] != "-" or inicioReparacion[5] != "-":
            print("⚠️ Debe usar "-" para separar (DD-MM-AAAA). ")
            continue
            
        partes = inicioReparacion.split("-")
                
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

        #PIDE FECHA FIN_________________________________________

    while True:
        finReparacion=input("Ingrese la fecha estimada de fin de reparación (ejemplo: 15-01-2026):").strip()
        if len(finReparacion) != 10:
            print("⚠️ Formato incorrecto. Debe ser DD/MM/AAAA (ej: 15-01-2026)")
            continue
                
        if finReparacion[2] != "-" or finReparacion[5] != "-":
            print("⚠️ Debe usar "-" para separar (DD-MM-AAAA). ")
            continue
            
        partes = finReparacion.split("-")
                
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

    observaciones= input("Comente alguna observacion necesaria para la reparación:")
    guardarReparaciones(inventario)
    print("Herramienta registrada en reparación correctamente.")


#________________________________________________________________________

def menuReparaciones(inventario):

    while True:
        print("\033[96m")
        print("""
        ╭─────────────────────────────────╮
                CONTROL REPARACIÓN   
        ╰─────────────────────────────────╯
            1 → Enviar a reparación
            2 → Salir
            """)
        print("\033[0m")
        
        opcion= input("🎯 Seleccione la opción para continuar:").strip()
        if opcion =="1":
            controlReparacion(inventario)
        elif opcion =="2": 
            print("SALIENDO... ")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menuReparaciones('inventario')