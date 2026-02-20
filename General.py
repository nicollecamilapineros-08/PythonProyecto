#PROGRAMA PRINCIPAL para la gestión de préstamo de herramientas
#en el barrio Santa Ana

from Permisos.usuarios import menuUsuario
from Permisos.administrador import ingreso, menuAdmin
import Gestiones.GestionUsuarios as GestionUsuarios
import Gestiones.herramientas as herramientas
import Gestiones.GestionPrestamos as GestionPrestamos
##HOLA



def main(datos):
    datos = GestionUsuarios.cargarUsuarios()
    inventario = herramientas.cargarHerramientas()
    prestamos = GestionPrestamos.cargarPrestamos()
    while True:
        
        print("\033[96m")
        print("""
            ╭─────────────────────────────────╮
             SISTEMA DE HERRAMIENTAS SANTA ANA                                    
            ╰─────────────────────────────────╯
            1 → Administrador
            2 → Usuario
            3 → Salir
            """)
        print("\033[0m")


        opcion = input("🎯 Bienvenido, seleccione su rol correspondiente:").strip()

        if opcion == "1":
            if ingreso(datos):
                menuAdmin(datos, inventario, prestamos)  
        elif opcion == "2":
                menuUsuario(inventario, prestamos)
    
        elif opcion=="3":
            print("SALIENDO...")
            print("Vuelva pronto.")
            break
        else:
            print("⚠️ Opción inválida. Intente nuevamente.")
    input("Presione cualquier tecla para continuar...")
            
main('datos')