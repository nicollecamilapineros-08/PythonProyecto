#INVENTARIO_____________________________________

import json
from Otros.Logs import registrarLog

def cargarHerramientas(nom_archivo="registroHerramientas.json"):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
            inventario = { 
                "listaHerramientas": [
            {
            "idHerramienta": "01",
            "nombre": "Taladro",
            "categoria": "construccion",
            "estado": "activa",
            "cantidad disponible": 5,
            "valor estimado": 50000
        },
        {
            "idHerramienta": "02",
            "nombre": "Pala",
            "categoria": "jardinería",
            "estado": "fuera de servicio",
            "cantidad disponible": 0,
            "valor estimado": 25000
        },
        {
            "idHerramienta": "03",
            "nombre": "Destornillador electrico",
            "categoria": "construccion",
            "estado": "en reparacion",
            "cantidad disponible": 5,
            "valor estimado": 70000
        }]
    }
    guardarHerramientas(inventario)
    return inventario

    
def guardarHerramientas(inventario, nom_archivo="registroHerramientas.json"):
    try:
        with open(nom_archivo, "w") as arch:
            json.dump(inventario, arch, indent=4)
    except Exception:
        inventario = {}
        print("✔️ Informacion guardada exitosamente.")

#MENU GESTION HERRAMIENTAS______________________________________

def menuGestionHerramientas(inventario):
    while True:
        
        print("""\033[38;5;213m
        ----------------------------------
                GESTIÓN HERRAMIENTAS
        ----------------------------------
            
        1 → Registrar herramientas
        2 → Lista de herramientas
        3 → Buscar herramienta
        4 → Actualizar herramienta
        5 → Eliminar herramienta
        6 → Guardar y salir
        \033[0m""")
        print()

        opcion= input("🎯 Seleccione la opción que desea ejecutar:")

        if opcion=="1":
            aggHerramienta(inventario)
        elif opcion=="2":
            listarHerramientas(inventario)
        elif opcion=="3":
            buscarHerramienta(inventario)
        elif opcion=="4":
            actualizarHerramienta(inventario)
        elif opcion=="5":
            eliminarHerramienta(inventario)
        elif opcion=="6":
            guardarHerramientas(inventario)
            print("✔️ SALIENDO...")
            break
        else:
            print("⚠️ Opción inválida. Intente nuevamente.")

        input("Presione cualquier tecla para continuar...")



#--------------------------------------------------------------------------------

#CREAR HERRAMIENTA______________________________

def aggHerramienta(inventario):
    print("""\033[3m
        REGISTRO DE HERRAMIENTAS
    -------------------------------
    \033[0m""")

    idHerramienta=input(" 🆔 ID de la nueva herramienta:").strip()

    if idHerramienta in inventario["listaHerramientas"]:
        print(f"⚠️ Error. La herramienta con ID: {idHerramienta} ya existe.")
        return 
    
    while True:
        numeroHerramientas =(int(input("🎯 Ingrese la cantidad de herramientas a registrar:")))
        if numeroHerramientas>0:
            break
        print("⚠️ Es necesario que se digite un número mayor a 0")
    
    for i in range(numeroHerramientas):

        while True:
            idHerramienta=input(" 🆔 ID de la nueva herramienta:").strip()
            if idHerramienta.isdigit():
                break
            print("⚠️  ID inválido. Intente nuevamente.")

        while True:
            nombreHerramienta=input("→ NOMBRE:")
            if nombreHerramienta.isalpha():
                break
            print("⚠️El nombre de la herramienta no puede estar compuesto por digitos.")
        
        while True:
            categoria=input("→ CATEGORÍA:")
            if categoria.isalpha():
                break
            print("⚠️ La categoría no puede estar compuesta por dígitos. Intente nuevamente.")

        while True:
            estado=input("→ ESTADO:")
            if estado.isalpha():
                break
            print("⚠️ Estados válidos: (activa, en reparación, fuera de servicio).") 
        
        while True:
            cantidadDisponible=input("→ Cantidad disponible:")
            if cantidadDisponible.isdigit():
                break
            print("⚠️  Asegurese de ingresar dígitos.") 

        while True:
            valorEstimado=(input("→ Valor estimado:"))
            if valorEstimado.isdigit():
                break
            print("⚠️ Asegurese de ingresar dígitos.") 

        herramientaNueva = {
        "idHerramienta": idHerramienta,
        "nombre": nombreHerramienta,
        "estado": estado,
        "categoria": categoria,
        "valor estimado": valorEstimado,
        "cantidad disponible": cantidadDisponible
        }
        inventario["listaHerramientas"].append(herramientaNueva)
        print(f"✔️  Herramienta {nombreHerramienta} registrada exitosamente.")
        registrarLog(f"Herramienta registrada: {nombreHerramienta} (ID: {idHerramienta})")
        input("Presione cualquier tecla para continuar...")

    guardarHerramientas(inventario)
    return inventario


#LISTAR HERRAMIENTAS_____________________________________________________

def listarHerramientas(inventario):

    print("""\033[3m
      LISTA DE HERRAMIENTAS
    -------------------------
    \033[0m""")

    if not inventario["listaHerramientas"]:
        print("⚠️ No hay herramientas registradas.")
        return
    
    print(f"{'ID':<8} {'NOMBRE':<25} {'ESTADO':<20} {'CATEGORÍA':<18} {'DISPONIBLES':<15} {'VALOR':<15}")
    print("─" * 101)

    for herramienta in inventario["listaHerramientas"]:
        print(f"{herramienta['idHerramienta']:<8} "
              f"{herramienta['nombre']:<25} "
              f"{herramienta['estado']:<20} "
              f"{herramienta['categoria']:<18} "
              f"{str(herramienta['cantidad disponible']):<15} "
              f"{herramienta['valor estimado']:<15}")
    
    print("─" * 101)
    print(f"✔️  Total de herramientas: {len(inventario['listaHerramientas'])}")
    


#BUSCAR HERRAMIENTA______________________________________

def buscarHerramienta(inventario):
    print("""\033[3m
        BUSCAR HERRAMIENTA
    --------------------------
    \033[0m""")

    if not inventario["listaHerramientas"]:
        print("⚠️ No hay herramientas registradas.")
        return
    
    idHerramienta = input("Ingrese el ID de la herramienta: ").strip()

    encontrada = None

    for herramienta in inventario["listaHerramientas"]:
        if herramienta["idHerramienta"] == idHerramienta:
            encontrada = herramienta
            break
    

    if encontrada:

        print("\033[38;5;153m")
        print("="*50)
        print(f"🎯 ESTADO DE HERRAMIENTA {encontrada['idHerramienta']}")
        print("="*50)
        print(f"Nombre: {encontrada['nombre']}")
        print(f"Estado: {encontrada['estado']}")
        print(f"Valor estimado: ${encontrada['valor estimado']}")
        print(f"Cantidad disponible: {encontrada['cantidad disponible']} unidades")
        print(f"Categoría: {encontrada['categoria']}")
        print("="*50)
        print("\033[0m") 

    else:
        print("⚠️ Herramienta no encontrada.")

#ACTUALIZAR HERRAMIENTA_____________________________________

def actualizarHerramienta(inventario):
    print("""\033[3m
        ACTUALIZAR HERRAMIENTA
     ---------------------------
     \033[0m""")
    
    if not inventario["listaHerramientas"]:
        print(f"⚠️ No hay herramientas registradas.")
        return
    
    idHerramienta=input("🆔 Ingrese el ID de la herramienta que desea actualizar:")

    herramientaBuscada= None
    encontrada=False
    posicion = 0

    for i in range(len(inventario["listaHerramientas"])):
        if inventario["listaHerramientas"][i]["idHerramienta"]== idHerramienta:
            herramientaBuscada= inventario["listaHerramientas"][i]
            posicion = i
            encontrada=True
            break

    if not encontrada:
        print(f"⚠️ No se encontró herramienta con ID {idHerramienta} en el sistema.")
        return
    
    print("-------------------------------")
    print("/n HERRAMIENTA A ACTUALIZAR:")
    print("-------------------------------")

    print( "-" *30)
    print(f"  ID                   : {herramientaBuscada['idHerramienta']}")
    print(f"  nombre               : {herramientaBuscada['nombre']}")
    print(f"  estado               : {herramientaBuscada['estado']}")
    print(f"  categoría            : {herramientaBuscada['categoria']}")
    print(f"  cantidad disponible  : {herramientaBuscada['cantidad disponible']}")
    print(f"  valor estimado       : {herramientaBuscada['valor estimado']}")
    print( "-" *30)
    print()
    print("🎯 Ingresa los nuevos datos:")


    while True:
        nombreHerramienta=input("→ NOMBRE:")
        if nombreHerramienta.isalpha():
            break
        print("⚠️El nombre de la herramienta no puede estar compuesto por digitos.")
        
    while True:
        categoria=input("→ CATEGORÍA:")
        if categoria.isalpha():
            break
        print("⚠️ La categoría no puede estar compuesta por dígitos. Intente nuevamente.")

    while True:
        estado=input("→ ESTADO:").lower()
        if estado.isalpha():
            break
        print("⚠️ Estados válidos: (activa, en reparación, fuera de servicio).") 
        
    while True:
        cantidadDisponible=(input("→ Cantidad disponible:"))
        if cantidadDisponible.isdigit():
            break
        print("⚠️ Asegurese de ingresar dígitos.") 

    while True:
        valorEstimado=(input("→ Valor estimado:"))
        if valorEstimado.isdigit():
            break
        print("⚠️ Asegurese de ingresar dígitos.")


    inventario["listaHerramientas"][posicion] = {
                "idHerramienta": idHerramienta,
                "nombre": nombreHerramienta,
                "estado": estado,
                "valor estimado": valorEstimado,
                "cantidad disponible": cantidadDisponible,
                "categoria": categoria
                }
    print("✔️ Herramienta actualizada exitosamente.")
    registrarLog(f"Herramienta actualizada: {nombreHerramienta} (ID: {idHerramienta})")
    guardarHerramientas(inventario)
    return inventario

#ELIMINAR HERRAMIENTA____________________________________________________

def eliminarHerramienta(inventario):

    print("""\033[3m
        ELIMINAR HERRAMIENTA
    ----------------------------
    \033[0m""")

    if not inventario["listaHerramientas"]:
        print(f"⚠️ No hay herramientas registradas.")
        return
    
    idHerramienta = input("🆔 ID de la herramienta a eliminar: ").strip()

    usuarioBuscado = None
    posicion = 0

    for i, herramienta in enumerate(inventario["listaHerramientas"]):
        if herramienta["idHerramienta"] == idHerramienta:
            usuarioBuscado = herramienta
            posicion = i
            break

    if usuarioBuscado is None:
            print(f"⚠️ No se encontró usuario con ID '{idHerramienta}'.")
            return
        
    print("---------------------------")
    print("\n HERRAMIENTA A ELIMINAR:")
    print("---------------------------")
    print( "-" *30)
    print(f"  ID                   : {herramienta['idHerramienta']}")
    print(f"  nombre               : {herramienta['nombre']}")
    print(f"  estado               : {herramienta['estado']}")
    print(f"  categoría            : {herramienta['categoria']}")
    print(f"  cantidad disponible  : {herramienta['cantidad disponible']}")
    print(f"  valor estimado       : {herramienta['valor estimado']}")
    print( "-" *30)

    
    confirmar = input("👀¿Está seguro que desea eliminar esta herramienta? (si/no): ").lower()
    
    if confirmar == 'si':
        herramientaEliminada = inventario["listaHerramientas"].pop(posicion)
        print(f"✔️ Herramienta '{herramientaEliminada['nombre']}' eliminada exitosamente.")
        registrarLog(f"Herramienta eliminada: {herramientaEliminada['nombre']} (ID: {idHerramienta})")
    else:
        print("⚠️ Operación cancelada. La herramienta no fue eliminada.")
    guardarHerramientas(inventario)  
    return inventario          