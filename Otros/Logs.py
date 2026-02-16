#FUNCION LOGS

def registrarLog(mensaje):
    try:
        from datetime import datetime
        #REDACTA FECHA Y HORA COMO TEXTO: 
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo = open("logs.txt", "a", encoding="utf-8")
        archivo.write(f"[{fecha_hora}] {mensaje}\n")
        archivo.close()
    except:
        pass

def verLogs():
    print("""\033[3m
        REGISTRO DE LOGS
    ----------------------------
    \033[0m""")
    
    #EL ENCODING PERMITE LEER DISTINTOS CARACTERES:

    try:
        archivo = open("logs.txt", "r", encoding="utf-8")
        contenido = archivo.read()
        archivo.close()
        
        if contenido:
            print(contenido)
        else:
            print("⚠️ No hay logs registrados aún.")
    
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo de logs.")
    except Exception as e:
        print(f"❌ Error al leer logs: {e}")