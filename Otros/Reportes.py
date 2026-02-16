#REPORTES

def menuReportes(inventario, prestamos):
    while True:
        print("\033[38;5;213m") 
        print("""
        ----------------------------------
                    REPORTES 
        ----------------------------------
        
         1 → Stock bajo (menos de 3)
         2 → Préstamos vencidos
         3 → Historial de un usuario
         4 → Herramientas más pedidas
         5 → Usuarios más activos
         6 → Volver
              
        \033[0m""")
        print()

        opcion= input("🎯Seleccione la opción que desea ejecutar:")

        if opcion=="1":
            stockBajo(inventario)
        elif opcion=="2":
            prestamosVencidos(prestamos)
        elif opcion=="3":
            historialUsuarios(prestamos)
        elif opcion=="4":
            herramientasMasPedidas(prestamos)
        elif opcion=="5":
            usuariosMasActivos(prestamos)
        elif opcion=="6":
            print("""✔️ La información ha sido guardada con exito. 
                Saliendo... Vuelva pronto.""")            
            break
        else:
            print("⚠️ Opción inválida. Intente nuevamente.")

        input("Presione cualquier tecla para continuar...")

#STOCK BAJO_________________________________________________________
#MENOS DE 3 UNIDADES DISPONIBLES

def stockBajo(inventario):
    print("\033[95m" + "=" * 55)
    print("🛠️ HERRAMIENTAS CON STOCK BAJO".center(55))
    print("=" * 55 + "\033[0m")  
    
    #REVISION DE HERRAMIENTAS CON POCAS UNIDADES:

    pocasUnidades = []
    for unidades in inventario["listaHerramientas"]:
        if int(unidades["cantidad disponible"]) < 3:
            pocasUnidades.append(unidades)
    
    if not pocasUnidades:
        print("✔️ Stock suficiente en inventario.")
        return
    
    print("\033[95m")
    print(f"{'ID':<8} {'NOMBRE':<20} {'DISPONIBLE':<12}")
    print("─" * 55)
    
    for unidades in pocasUnidades:
        print(f"{unidades['idHerramienta']:<8} {unidades['nombre']:<20} {unidades['cantidad disponible']:<12}")
    
    print("=" * 55 + "\033[0m")  
    
#PRÉSTAMOS VENCIDOS____________________________________________________

def prestamosVencidos(prestamos):

    print("\033[95m" + "=" * 55)
    print("🛠️ PRÉSTAMOS VENCIDOS".center(55))
    print("=" * 55 + "\033[0m")  


    #COMPARAR FECHAS:

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

#HISTORIAL USUARIOS____________________________________________________

def historialUsuarios(prestamos):

    print("\033[95m" + "=" * 55)
    print("🛠️ HISTORIAL DE USUARIOS".center(55))
    print("=" * 55 + "\033[0m") 
    
    idUsuario = input("🆔 Ingrese el ID del usuario a consultar: ").strip()
    
    #RECOPILAR PRESTAMOS DEL USUARIO:

    historial = []
    for i in prestamos["listaPrestamos"]:
        if i["idUsuario"] == idUsuario:
            historial.append(i)
    
    if not historial:
        print(F"⚠️ El usuario con ID {idUsuario} tiene historial vacío.")
        return
    
    print("\033[95m")
    print(f"\n{'ID':<8} {'HERRAMIENTA':<20} {'ESTADO':<12}")
    print("─" * 55)
    
    for i in historial:
        print(f"{i['idPrestamo']:<8} {i['nombreHerramienta']:<20} {i['estado']:<12}")
    
    print("\033[95m" + "=" * 55)

#HERRAMIENTAS MÁS PEDIDAS________________________________________________________

def herramientasMasPedidas(prestamos):

    print("\033[95m" + "=" * 55)
    print("🛠️ HERRAMIENTAS MÁS PEDIDAS".center(55))
    print("=" * 55 + "\033[0m") 


    #CONTAR CUANTAS VECES SE PRESTÓ:

    total = {}

    for i in prestamos["listaPrestamos"]:
        herramienta = i["nombreHerramienta"]
        if herramienta not in total:
            total[herramienta] = 0
        total[herramienta] += 1
    
    if not total:
        print("⚠️ No hay historial de préstamos.")
        return
    
    print("\033[95m")
    print(f"{'HERRAMIENTA':<25} {'VECES':<10}")
    print("─" * 55)
    
    for nombre, veces in total.items():
        print(f"{nombre:<25} {veces:<10}")
    
    print("=" * 55 + "\033[0m") 

#USUARIOS MÁS ACTIVOS_______________________________________________________

def usuariosMasActivos(prestamos):

    print("\033[95m" + "=" * 55)
    print("USUARIOS MÁS ACTIVOS".center(55))
    print("=" * 55 + "\033[0m") 

    total = {}
    for i in prestamos["listaPrestamos"]:
        usuario = i["idUsuario"]
        if usuario not in total:
            total[usuario] = 0
        total[usuario] += 1
    
    if not total:
        print("⚠️ No hay historial de préstamos.")
        return
    
    print("\033[95m")
    print(f"{'USUARIO':<25} {'PRÉSTAMOS':<12}")
    print("─" * 55)
    for usuario, cantidad in total.items():
        print(f"{usuario:<25} {cantidad:<12}")
    print("=" * 55 + "\033[0m") 