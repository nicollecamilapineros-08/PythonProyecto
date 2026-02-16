#ADMIN OPCION 1: GESTIÓN DE USUARIOS

import json
from Otros.Logs import registrarLog

def cargarUsuarios(nom_archivo="registroUsuarios.json"):
    try:
        with open (nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
            listaInicial= {
            "usuarios": [
            {
                "idUsuario": "001",
                "nombre": "Marcos",
                "apellido": "Cepeda",
                "telefono": "3248746598",
                "direccion": "Cra 8 #97-03",
                "tipo": "administrador"
            },
            {
                "idUsuario": "002",
                "nombre": "Lidia",
                "apellido": "Perez",
                "telefono": "3148745968",
                "direccion": "Calle 21 #33-98",
                "tipo": "residente"
            }
            ]
            }
    guardarUsuarios(listaInicial)
    return listaInicial
    
def guardarUsuarios(usuario, nom_archivo="registroUsuarios.json"):
    try:
        with open (nom_archivo, "w") as arch:
            json.dump(usuario, arch, indent=4)
    except Exception:
        usuario = {}
        print("Informacion guardada exitosamente.")

########  MENU GESTION USUARIOS 

def menuGestionUsuarios(datos):
    while True:
        print("\033[38;5;213m") 
        print("""
        ----------------------------------
                GESTIÓN USUARIOS
        ----------------------------------
        
        1 → Registrar usuarios
        2 → Lista de usuarios
        3 → Buscar usuario
        4 → Actualizar usuario
        5 → Eliminar usuario
        6 → Guardar y salir
              
        \033[0m""")
        print()

        opcion= input("🎯Seleccione la opción que desea ejecutar:")

        if opcion=="1":
            registroUsuarios(datos)
        elif opcion=="2":
            listarUsuarios(datos)
        elif opcion=="3":
            buscarUsuario(datos)
        elif opcion=="4":
            actualizarUsuario(datos)
        elif opcion=="5":
            eliminarUsuario(datos)
        elif opcion=="6":
            guardarUsuarios(datos)
            print("✔️ SALIENDO...")
            break
        else:
            print("⚠️ Opción inválida. Intente nuevamente.")

        input("Presione cualquier tecla para continuar...")
#CREAR USUARIOS____________________________________________________________________________________

def registroUsuarios(datos):

    print("""\033[3m
        REGISTRO DE USUARIOS
    ---------------------------
    \033[0m""")

    while True:
        numeroUsuarios =(int(input("🎯 Ingrese la cantidad de usuarios que desea registrar:")))
        if numeroUsuarios>0:
            break
        print("⚠️ Es necesario que se digite un número mayor a 0")
    
    for i in range(numeroUsuarios):

        while True:
            idUsuario=input(" 🆔 ID del nuevo usuario:").strip()
            if idUsuario.isdigit():
                break
            print("⚠️  ID inválido. Intente nuevamente.")

        while True:
            nombreUsu=input("→NOMBRE:")
            if nombreUsu.isalpha():
                break
            print("⚠️El nombre del usuario no puede estar compuesto por digitos.")
        
        while True:
            apellidoUsu=input("→APELLIDO:")
            if apellidoUsu.isalpha():
                break
            print("⚠️El apellido no puede estar compuesto por dígitos. Intente nuevamente.")
            
        while True:
            telefonoUsu=input("→TELÉFONO:")
            if telefonoUsu.isdigit() and len(telefonoUsu) == 10:
                break
            print("⚠️Cantidad inválida de dígitos. Intente nuevamente.")
        
        while True:
            tipoUsuario=input("→TIPO (residente/administrador):").lower().strip()
            if tipoUsuario in ["residente", "administrador"]:
                break
            print("⚠️Tipo de usuario incorrecto. Intente nuevamente.")
            
        direccionUsu = input("→DIRECCIÓN:").strip()
        usuNuevo = {
            "idUsuario": idUsuario,
            "nombre": nombreUsu,
            "apellido": apellidoUsu,
            "telefono": telefonoUsu,
            "direccion": direccionUsu,
            "tipo": tipoUsuario
            }
        datos["usuarios"].append(usuNuevo)
        print(f"✔️  Usuario {nombreUsu} {apellidoUsu} registrado exitosamente.")
    
    registrarLog(f"Usuario registrado: {nombreUsu} {apellidoUsu} (ID: {idUsuario})") 

#LISTAR USUARIOS__________________________________________________________________________________

def listarUsuarios(datos):
    print("""\033[3m
        LISTA DE USUARIOS
    -------------------------
    \033[0m""")
    if not datos["usuarios"]:
        print("No hay usuarios registrados.")
        return
    
    print(f"{'ID':<8} {'NOMBRE':<15} {'APELLIDO':<15} {'TELÉFONO':<15} {'DIRECCIÓN':<25} {'TIPO':<18}")
    print("─" * 115)

    for usuario in datos["usuarios"]:
      print(f"{usuario['idUsuario']:<8} "
            f"{usuario['nombre']:<15} "
            f"{usuario['apellido']:<15} "
            f"{usuario['telefono']:<15} "
            f"{usuario['direccion']:<25} "
            f"{usuario['tipo']:<18}")
    
    print("─" * 115)
    print(f"✔️  Total de usuarios: {len(datos['usuarios'])}")


#BUSCAR USUARIO______________________________________________________

def buscarUsuario(datos):
    print("""\033[3m
         BUSCAR USUARIO
    -------------------------
    \033[0m""")

    if not datos["usuarios"]:
        print("⚠️ No hay usuarios registrados ahora.")
        return
    id = input("🆔 Ingrese el ID del usuario:").strip()

    usuarioBuscado= None
    for usuario in datos["usuarios"]:
        if usuario["idUsuario"] == id:
            usuarioBuscado=usuario
            break

    if usuarioBuscado:
        print("─" * 40)
        print(f"  {'ID':<18} : {usuarioBuscado['idUsuario']}")
        print(f"  {'nombre':<18} : {usuarioBuscado['nombre']}")
        print(f"  {'apellido':<18} : {usuarioBuscado['apellido']}")
        print(f"  {'telefono':<18} : {usuarioBuscado['telefono']}")
        print(f"  {'direccion':<18} : {usuarioBuscado['direccion']}")
        print(f"  {'tipo':<18} : {usuarioBuscado['tipo']}")
        print("─" * 40)
    else:
        print(f"⚠️ No se encontró ningún usuario con el ID {id}")


#ACTUALIZAR USUARIO_______________________________________________________

def actualizarUsuario(datos):
    
    print("""\033[3m
        ACTUALIZAR USUARIO
     -------------------------
     \033[0m""")

    if not datos["usuarios"]:
        print(f"⚠️ No hay usuarios registrados")
        return
    
    id = input("🆔 Ingrese el ID del usuario que desea actualizar:")

    usuarioBuscado= None
    posicion = 0
    encontrado = False

    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["idUsuario"]== id:
            usuarioBuscado= datos["usuarios"][i]
            posicion = i
            encontrado=True
            break

    if not encontrado:
        print(f"⚠️ No se encontró usuario con ID {id} en el sistema.")
        return

    print( "----------------------")
    print("\nUSUARIO A ACTUALIZAR:")
    print("------------------------")

    print( "-" *30)
    print(f"  ID         : {usuarioBuscado['idUsuario']}")
    print(f"  nombre     : {usuarioBuscado['nombre']}")
    print(f"  apellido   : {usuarioBuscado['apellido']}")
    print(f"  telefono   : {usuarioBuscado['telefono']}")
    print(f"  dirección  : {usuarioBuscado['direccion']}")
    print(f"  tipo       : {usuarioBuscado['tipo']}")
    print( "-" *30)
    print()
    print("🎯 Ingresa los nuevos datos:")
    while True:
        nombre = input("→ NOMBRE: ").strip()
        if nombre.isalpha():
            break
        print("⚠️El nombre del usuario no puede estar compuesto por digitos.")

    while True:
        apellido = input("→ APELLIDO: ").strip()
        if apellido.isalpha():
            break
        print("⚠️El apellido no puede estar compuesto por dígitos. Intente nuevamente.")

    while True:
        telefono = input("→ TELÉFONO (10 dígitos): ").strip()
        if telefono.isdigit() and len(telefono) == 10:
            break
        print("⚠️ El teléfono debe tener 10 dígitos.")
        
    direccion = input("→ DIRECCIÓN: ").strip()
        
    while True:
        tipo = input("→ TIPO (residente/administrador): ").lower().strip()
        if tipo in ["residente", "administrador"]:
            break
        print("⚠️ Tipo de usuario inválido. Intente nuevamente.")
   
    datos["usuarios"][posicion] = {
        "idUsuario": id,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "direccion": direccion,
        "tipo": tipo
        }
    guardarUsuarios(datos)
    print(f"✔️ Usuario '{nombre} {apellido}' actualizado correctamente.")
    registrarLog(f"Usuario actualizado: {nombre} {apellido} (ID: {id})")
       
#ELIMINAR USUARIO________________________________________________
def eliminarUsuario(datos):
     
    print("""\033[3m
        ELIMINAR USUARIO
    -------------------------
    \033[0m""")

    if not datos["usuarios"]:
        print("⚠️ No hay usuarios registrados")
        return

    id = input("🆔 Ingrese el ID del usuario que desea eliminar: ")

    usuarioBuscado = None
    posicion = 0

    for i, usuario in enumerate(datos["usuarios"]):
        if usuario["idUsuario"] == id:
            usuarioBuscado = usuario
            posicion = i
            break

    if usuarioBuscado is None:
            print(f"⚠️ No se encontró usuario con ID '{id}'.")
            return
    
    print( "----------------------")
    print("\nUSUARIO A ELIMINAR:")
    print("------------------------")

    print( "-" *30)
    print(f"  ID         : {usuario['idUsuario']}")
    print(f"  nombre     : {usuario['nombre']}")
    print(f"  apellido   : {usuario['apellido']}")
    print(f"  telefono   : {usuario['telefono']}")
    print(f"  dirección  : {usuario['direccion']}")
    print(f"  tipo       : {usuario['tipo']}")
    print( "-" *30)
    print()

    confirmar = input("👀¿Está seguro que desea eliminar este producto? (si/no): ").lower()
        
    if confirmar == 'si':
        usuarioEliminado = datos["usuarios"].pop(posicion)
        print(f"✔️ Usuario '{usuarioEliminado['nombre']}' eliminado exitosamente.")
        registrarLog(f"Usuario eliminado: {usuarioEliminado['nombre']} (ID: {usuarioEliminado['idUsuario']})") 

        guardarUsuarios(datos)
    else:
        print(" ⚠️ Proceso cancelado.")


