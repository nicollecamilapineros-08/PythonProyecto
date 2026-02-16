#  Sistema de Gestión de Herramientas Comunitarias - Santa Ana


En muchos barrios existe la costumbre de compartir herramientas entre vecinos para evitar que cada persona tenga que comprarlas todas. El problema es que, con el tiempo, se pierde el control: algunas herramientas no se devuelven a tiempo, otras se dañan y no se sabe quién las tiene, o simplemente no hay registro claro de cuántas hay disponibles. El sistema registra las herramientas, los vecinos y los préstamos realizados. Con esta solución, esperan que cualquier integrante de la comunidad pueda consultar la información sin depender de cuadernos ni llamadas telefónicas.


#  Descripción

Este sistema permite a los residentes de una comunidad solicitar préstamos de herramientas de uso común (taladros, palas, martillos, etc.) de forma organizada. Los administradores pueden gestionar el inventario, aprobar solicitudes y generar reportes del uso de las herramientas.



#  Cómo Usar

## Como Administrador:

1. Ejecutar: `python General.py`
2. Seleccionar: `1` (Administrador)
3. Ingresar ID: `001`
4. Opciones disponibles:
   - Gestión de usuarios
   - Gestión de herramientas
   - Gestión de préstamos 
   - Reportes 
   - Ver logs del sistema

## Como Usuario/Residente:

1. Ejecutar: `python General.py`
2. Seleccionar: `2` (Usuario)
3. Ingresar tu ID (ej: `002`)
4. Opciones disponibles:
   - Ver herramientas disponibles
   - Buscar herramienta por ID
   - Solicitar préstamo
   - Ver mis préstamos


#  Funcionalidades Principales

### Módulo Administrador
- Gestión de usuarios (CRUD completo)
- Gestión de herramientas (CRUD completo)
- Aprobación/rechazo de solicitudes de préstamo
- Registro de devoluciones
- Generación de reportes:
     - Stock bajo (menos de 3 unidades)
     - Préstamos activos y vencidos
     - Historial de préstamos por usuario
     - Herramientas más solicitadas
     - Usuarios más activos
- Visualización de logs del sistema

### Módulo Usuario/Residente
- Consultar herramientas disponibles
- Buscar herramienta por ID (ver estado y disponibilidad)
- Crear solicitudes de préstamo
- Ver estado de mis préstamos

###  Sistema de Logs
- Registro automático de eventos importantes
- Registro de errores (ej: intentos de préstamo sin stock)
- Trazabilidad completa de operaciones



