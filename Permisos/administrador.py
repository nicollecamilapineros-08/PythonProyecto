from Gestiones.GestionUsuarios import menuGestionUsuarios, guardarUsuarios
from Gestiones.herramientas import menuGestionHerramientas, guardarHerramientas
from Gestiones.GestionPrestamos import menuGestionPrestamos, guardarPrestamos
from Otros.Reportes import menuReportes
from Otros.Logs import registrarLog, verLogs

#VALIDAR USUARIO_______________________________________________________________

def ingreso(datos):  
    print("""\033[38;5;213m
    
    ----------------------------------
        VALIDACIÓN DE ADMINISTRADOR
    ----------------------------------

    \033[0m""")
    intentos = 3
    for i in range(intentos):
        idUsuario=input("🆔 Ingrese su ID para continuar:")
        usuarioHallado = None
        for usuario in datos["usuarios"]:
            if usuario["idUsuario"]== idUsuario:
                usuarioHallado = usuario
                break

        if usuarioHallado is None:
            print("⚠️ Usuario con ID {idUsuario} no identificado.")
            registrarLog(f"Intento de ingreso fallido: ID '{idUsuario}' no existe")

            if i< intentos-1:
                print(f"\033[1m {intentos - i - 1} intentos restantes.\033[0m")
            continue

        if usuarioHallado["tipo"] =="administrador":
            print(f"✔️ Bienvenido {usuarioHallado['nombre']} {usuarioHallado['apellido']}")
            registrarLog(f"Ingreso exitoso: {usuarioHallado['nombre']} {usuarioHallado['apellido']}")
            return True
        else:
            print("⚠️  Usuario no registrado como administrador.")
            registrarLog(f"Intento de ingreso sin permisos: {usuarioHallado['nombre']} no es administrador")
            return False
    print("⚠️ Alcanzó el límite de intentos de ingreso.")
    registrarLog("Bloqueo temporal: Se agotaron los intentos de ingreso")
    return False
        
        
#MENU ADMIN____________________________________________________________________

def menuAdmin(datos, inventario, prestamos):
        while True:
            print("\033[96m")
            print("""
            ╭─────────────────────────────────╮
                    MENÚ ADMINISTRADOR                                      
            ╰─────────────────────────────────╯
            1 → Gestión de usuarios
            2 → Gestión de herramientas
            3 → Gestión de préstamos
            4 → Consultas y reportes
            5 → Registro de eventos (logs)
            6 → Guardar y salir
                """)
            print("\033[0m")

            opcion= input("🎯 Seleccione la opción que deseas ejecutar:").strip()

            if opcion == "1":
                menuGestionUsuarios(datos)
            elif opcion == "2":
                menuGestionHerramientas(inventario)
            elif opcion == "3":
                menuGestionPrestamos(datos, inventario, prestamos)
            elif opcion =="4":
                menuReportes(inventario, prestamos)
            elif opcion=="5":
                verLogs()
            elif opcion =="6":
                guardarUsuarios(datos)
                guardarHerramientas(inventario)
                guardarPrestamos(prestamos)
                print("""✔️ La información ha sido guardada con exito. 
                    Saliendo... Vuelva pronto.""")
                break
            else:
                print("⚠️ Opción inválida. Intente nuevamente.")
            input("Presione cualquier tecla para continuar...")