
from process.gestordatosclimaticos import GestorDeDatosClimaticos

# Función para insertar una nueva ubicación con latitud y longitud
def insertar_ubicacion(gestor):
    try:
        print("Introduce la latitud y longitud de la ubicación:")

        # Solicitar y validar latitud
        lat = input("Latitud: ").strip()
        if not lat:
            print("Error: La latitud no puede estar vacía.")  # Validación: Latitud no puede estar vacía
            return
        try:
            lat = float(lat)  # Intentar convertir la latitud a un número flotante
            if lat < -90 or lat > 90:
                print("Error: La latitud debe estar entre -90 y 90.")  # Validación: Latitud debe estar entre -90 y 90
                return
        except ValueError:
            print("Error: La latitud debe ser un número válido.")  # Error si no se introduce un número válido
            return

        # Solicitar y validar longitud
        lng = input("Longitud: ").strip()
        if not lng:
            print("Error: La longitud no puede estar vacía.")  # Validación: Longitud no puede estar vacía
            return
        try:
            lng = float(lng)  # Intentar convertir la longitud a un número flotante
            if lng < -180 or lng > 180:
                print("Error: La longitud debe estar entre -180 y 180.")  # Validación: Longitud debe estar entre -180 y 180
                return
        except ValueError:
            print("Error: La longitud debe ser un número válido.")  # Error si no se introduce un número válido
            return

        # Intentar insertar la ubicación en el gestor
        try:
            ubicacion_encontrada = gestor.insertar_nueva_ubicacion(lat, lng)
            if not ubicacion_encontrada:
                print(f"La ubicación '{lat}, {lng}' insertada correctamente.")  # Si la ubicación no existe se inserta correctamente
            else:
                print(f"La ubicación '{lat}, {lng}' ya existe.")  # Si la ubicación ya existe
        except Exception as e:
            print(f"Error al interactuar con el gestor: {e}")  # Captura cualquier error relacionado con la interacción con el gestor
            return

        # Obtener el número total de ubicaciones
        try:
            print(f"Número de ubicaciones actualmente: {gestor.get_numero_ubicaciones()}")
        except Exception as e:
            print(f"Error al obtener el número de ubicaciones: {e}")  # Error al obtener el número de ubicaciones

    except Exception as e:
        # Captura cualquier otro error inesperado
        print(f"Se ha producido un error inesperado: {e}")

# Función para buscar una ubicación por su código postal
def buscar_ubicacion(gestor):
    codigo_postal = input("Introduce el codigo postal que deseas buscar: ")
    
    # Buscar la ubicación en la lista de ubicaciones
    ubicacion = gestor.buscar_por_codigo_postal(codigo_postal)
    if ubicacion:
        print(f"Ubicación encontrada: {ubicacion.mostrar_informacion()}")
    else:
        print("Ubicación no encontrada.")

# Función para buscar ubicaciones por provincia
def buscar_ubicaciones_por_provincia(gestor):
    provincia = input("Introduce la provincia que deseas buscar: ")
    
    # Buscar todas las ubicaciones que pertenecen a la provincia
    resultados = gestor.buscar_por_provincia(provincia)
    
    if resultados:
        print(f"Numero de ubicaciones en '{provincia}': {len(resultados)}")  # Muestra la cantidad de ubicaciones encontradas
        for ubicacion in resultados:
            ubicacion.mostrar_informacion()  # Muestra la información de cada ubicación encontrada
    

# Función para mostrar todos los códigos postales y provincias almacenadas
def mostrar_codigos_postales_y_provincias_almacenadas(gestor):
    print("================================================")
    gestor.mostrar_codigos_postales_y_provincias_almacenadas()  # Muestra los códigos postales y provincias almacenadas
    print("================================================")

# Función para buscar una ubicación por su latitud y longitud
def buscar_ubicacion_por_lat_lng(gestor):
    latitud = input("Introduce la latitud: ")
    longitud = input("Introduce la longitud: ")

    # Convertir latitud y longitud a flotantes (float)
    try:
        latitud = float(latitud)
        longitud = float(longitud)
    except ValueError:
        print("Error: La latitud y longitud deben ser números.")
        return
    
    # Buscar la ubicación por latitud y longitud
    ubicacion = gestor.buscar_por_latitud_longitud(latitud, longitud)
    if ubicacion:
        print(f"Ubicación encontrada: {ubicacion.mostrar_informacion()}")
    else:
        print("Ubicación no encontrada.")


# Bloque principal de ejecución
if __name__ == "__main__":
    # Crear el gestor de datos y obtener la información
    gestor = GestorDeDatosClimaticos()
    
    # Bucle principal para mostrar el menú y permitir al usuario elegir acciones
    while True:
        print("================================================================")
        print("\nMenú Principal")
        print("1. Insertar una ubicación")
        print("2. Buscar una ubicación")
        print("3. Buscar ubicaciones por provincia")
        print("4. Mostrar provincias y CP almacenados")
        print("5. Buscar una ubicacion por latitud y longitud.")
        print("Escribe 'exit' para salir.")
        
        opcion = input("Selecciona una opción: ").strip().lower()

        # Ejecutar la función correspondiente según la opción seleccionada
        if opcion == '1':
            insertar_ubicacion(gestor)  # Insertar una ubicación
        elif opcion == '2':
            buscar_ubicacion(gestor)  # Buscar una ubicación
        elif opcion == '3':
            buscar_ubicaciones_por_provincia(gestor)  # Buscar ubicaciones por provincia
        elif opcion == '4':
            mostrar_codigos_postales_y_provincias_almacenadas(gestor)  # Mostrar códigos postales y provincias almacenadas
        elif opcion == '5':
            buscar_ubicacion_por_lat_lng(gestor)  # Buscar una ubicación por latitud y longitud
        elif opcion == 'exit':
            print("Saliendo del programa.")  # Mensaje al salir del programa
            break  # Termina el bucle y sale del programa
        else:
            print("Opción no válida. Inténtalo de nuevo.")  # Si la opción no es válida